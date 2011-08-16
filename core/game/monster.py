from game.creature import Creature, CreatureBase, uniqueId
import game.engine, game.map, game.scriptsystem
from packet import TibiaPacket
import copy, random, time
from twisted.internet import reactor
from twisted.internet.task import LoopingCall
from twisted.python import log
import game.enum
import game.errors
import game.item
import config

monsters = {}
class Monster(Creature):
    def generateClientID(self):
        return 0x40000000 + uniqueId()
        
    def __init__(self, base, position, cid=None):
        Creature.__init__(self, base.data, position, cid)
        self.base = base
        self.creatureType = 1
        self.spawnPosition = position[:]
        self.lastStep = 0
        self.speed = float(self.base.speed)
        self.lastMelee = 0
        self.walkPer = 3
        
    def onDeath(self):
        # Transform
        tile = game.map.getTile(self.position)

        corpse = game.item.Item(self.base.data["corpse"])
        corpse.decay(self.position)
        splash = game.item.Item(game.enum.FULLSPLASH)
        splash.fluidSource = game.enum.FLUID_BLOOD
        splash.decay(self.position)
        
        tile.placeItem(corpse)
        tile.placeItem(splash)
        try:
            tile.removeCreature(self)
        except:
            pass
        game.engine.updateTile(self.position, tile)
        
        if self.lastDamager and self.lastDamager.isPlayer():
            if self.lastDamager.data["stamina"] or config.noStaminaNoExp == False:
                self.lastDamager.modifyExperience(self.base.experience)

            if self.base.experience >= self.lastDamager.data["level"]:
                self.lastDamager.soulGain()
        Creature.onDeath(self)
        
    def say(self, message, messageType=game.enum.MSG_SPEAK_MONSTER_SAY):
        return Creature.say(self, message, messageType)
        
    def yell(self, message, messageType=game.enum.MSG_SPEAK_MONSTER_YELL):
        return Creature.yell(self, message, messageType)
        
class MonsterBase(CreatureBase):
    def __init__(self, data, brain, monsterData):
        self.data = data
        self.voiceslist = []
        self.brain = brain
        self.scripts = {"onFollow":[], "onTargetLost":[]}
        self.summons = []
        
        self.speed = 100
        self.experience = 0
        
        
        self.setBehavior()
        self.setImmunity()
        self.walkAround()
        self.bloodType()
        self.setTargetChance()
        
        self.meleeAttacks = []
        self.spellAttacks = []
        self.defenceSpells = []
        
    def spawn(self, position, place=True):
        monster = Monster(self, position, None)
        self.brain.beginThink(monster) # begin the heavy thought process!

        if self.targetChance and not (self.meleeAttacks or self.spellAttacks):
            log.msg("Warning: '%s' have targetChance, but no attacks!" % self.data["name"])
            
        if place:
                stackpos = game.map.getTile(position).placeCreature(monster)
                list = game.engine.getSpectators(position)
                for client in list:
                    stream = TibiaPacket()
                    stream.magicEffect(position, 0x03)
                    stream.addTileCreature(position, stackpos, monster, client.player)
            
                    stream.send(client)
        return monster
    def setHealth(self, health, healthmax=None):
        if not healthmax:
            healthmax = health
        self.data["health"] = health
        self.data["healthmax"] = healthmax
        
        return self

    def bloodType(self, color="blood"):
        self.blood = color #getattr(game.enum, 'FLUID_'+color.upper())

    def setOutfit(self, lookhead, lookbody, looklegs, lookfeet):
        self.data["lookhead"] = lookhead
        self.data["lookbody"] = lookbody
        self.data["looklegs"] = looklegs
        self.data["lookfeet"] = lookfeet
        
    def setDefense(self, armor=0, fire=1, earth=1, energy=1, ice=1, holy=1, death=1, physical=1, drown=1):
        self.armor = armor
        self.fire = fire
        self.earth = earth
        self.energy = energy
        self.ice = ice
        self.holy = holy
        self.death = death
        self.drown = drown
        self.physical = physical

    def setTargetChance(self, chance=10):
        self.targetChance = chance
    
    def setSummon(self, monster=None, chance=10, max=1):
        self.summons.append([monster, chance, max]) 
        
    def setExperience(self, experience):
        self.experience = experience
        
    def setSpeed(self, speed):
        self.speed = speed
        
    def setBehavior(self, summonable=0, attackable=1, hostile=1, illusionable=0, convinceable=0, pushable=0, pushItems=1, pushCreatures=1, targetDistance=1, runOnHealth=0):
        self.summonable = summonable
        self.attackable = attackable
        self.hostile = hostile
        self.illusionable = illusionable
        self.convinceable = convinceable
        self.pushable = pushable
        self.pushItems = pushItems
        self.pushCreaturse = pushCreatures
        self.targetDistance = targetDistance
        self.runOnHealth = runOnHealth
        
    def walkAround(self, energy=0, fire=0, poison=0):
        self.ignoreEnergy = energy
        self.ignoreFire = fire
        self.ignorePoison = poison
        
    def setImmunity(self, paralyze=1, invisible=1, lifedrain=1, drunk=1):
        self.paralyze = paralyze
        self.invisible = invisible
        self.lifedrain = lifedrain
        self.drunk = drunk
        
    def voices(self, *argc):
        self.voiceslist = tuple(argc)

    def regMelee(self, skill, attack, factor=1, level= 0, interval=config.meleeAttackSpeed, formula=config.meleeDamage):
        self.meleeAttacks.append([interval, formula, attack, skill, level, factor])
        
    def regTargetSpell(self, spellName, interval=1, chance=10, range=1, strength=1):
        self.spellAttacks.append([interval, spellName, chance, range, strength])
        
    def regSelfSpell(self, spellName, interval=1, chance=10, strength=1):
        self.defenceSpells.append([interval, spellName, chance, strength])
        
    def regBoost(self, ability, chance, change, duration):
        pass # TODO
        
class MonsterBrain(object):
    def beginThink(self, monster):
        self.handleThink(monster)
        if monster.base.voiceslist:
            self.handleTalk(monster)

    @game.engine.loopInThread(2)
    def handleThink(self, monster):
        # Are we alive?
        if not monster.alive:
            return False # Stop looper
            
        # Walking
        if monster.target: # We need a target for this code check to run
        
            # If target is out of sight, stop following it and begin moving back to base position
            if not monster.canSee(monster.target.position):
                monster.base.onTargetLost(monster.target)
                monster.target = None
                if monster.walkPer == 0.1:
                    monster.walkPer = 3
                    monster.setSpeed(monster.speed / 2)
                    
                game.engine.autoWalkCreatureTo(monster, monster.spawnPosition, 0, True) # Yes, last step might be diagonal to speed it up
                return
                
            elif monster.data["health"] <= monster.base.runOnHealth:
                monster.walkPer = 0.5
                monster.setSpeed(monster.speed * 2)
                
            elif monster.base.meleeAttacks and monster.inRange(monster.target.position, 1, 1):
                attack = random.choice(monster.base.meleeAttacks)
                if monster.lastAttack + attack[0] <= time.time():
                    dmg = -1 * random.randint(0, round(attack[1](attack[2], attack[3], attack[4], attack[5])))
                
                    monster.target.onHit(monster, dmg, game.enum.PHYSICAL)
                    monster.lastAttack = time.time()
                
                return # If we do have a target, we stop here
            
        # Only run this check if there is no target, we are hostile and targetChance checksout
        elif not monster.target and monster.base.hostile and monster.base.targetChance > random.randint(0, 100) and monster.data["health"] > monster.base.runOnHealth:
            spectators = game.engine.getSpectatorList(monster.position) # Get all creaturse in range
            if spectators: # If we find any
                target = None
                
                # Only run this code if there is more then one in range
                if len(spectators) > 1: 
                    bestDist = 0
                    for x in spectators:
                        # Calc x+y distance, diagonal is honored too.
                        dist = monster.distanceStepsTo(x.position) 
                        if dist < bestDist:
                            # If it's smaller then the previous value
                            bestDist = dist
                            target = x.player
                else:
                    # Target the singel spectator
                    target = spectators[0].player
                monster.target = target
                
                # Call the scripts
                monster.base.onFollow(monster.target)
                
                # Begin autowalking
                game.engine.autoWalkCreatureTo(monster, monster.target.position, -1 * monster.base.targetDistance, False)
                
                # If the target moves, we need to recalculate, if he moves out of sight it will be caught in next brainThink
                def __followCallback(who):
                    if monster.target == who:
                        monster.stopAction()
                        game.engine.autoWalkCreatureTo(monster, monster.target.position, -1 * monster.base.targetDistance, False)
                        monster.target.scripts["onNextStep"].append(__followCallback)
                        
                monster.target.scripts["onNextStep"].append(__followCallback)
                return # Prevent random walking
                
        if not monster.action and time.time() - monster.lastStep > monster.walkPer: # If no other action is available
            self.walkRandomStep(monster) # Walk a random step
            
    @game.engine.loopInThread(2)        
    def handleTalk(self, monster):
        # Are we alive?
        if not monster.alive:
            return False # Stop looper
            
        if 10 > random.randint(0, 100): # 10%
            # Find a random text
            text = random.choice(monster.base.voiceslist)
            
            # If text is uppercase, then yell it.
            if text.isupper():
                monster.yell(text)
            else:
                monster.say(text)
                
    def walkRandomStep(self, monster):
        # Ignore autowalking when there is noone in range
        spectators = game.engine.getSpectatorList(monster.position)
        if not spectators:
            return False
        
        # How far are we (x,y) from our spawn point?
        xFrom = monster.position[0]-monster.spawnPosition[0]
        yFrom = monster.position[1]-monster.spawnPosition[1]
        
        steps = [0,1,2,3]
        
        # Reorder the steps randomly
        random.shuffle(steps)
        
        for step in steps:
            # Prevent us from autowalking futher then 5 steps
            if step is 0:
                if monster.spawnPosition[1]-(monster.position[1]-1) > 5:
                    print "Stop by north"
                    print monster.position, " vs ", monster.spawnPosition
                    continue
            elif step is 1:
                if (monster.position[0]+1)-monster.spawnPosition[0] > 5:
                    print "Stop by east"
                    print monster.position, " vs ", monster.spawnPosition
                    continue
            elif step is 2:
                if (monster.position[1]+1)-monster.spawnPosition[1] > 5:
                    print "Stop by south"
                    print monster.position, " vs ", monster.spawnPosition
                    continue
            elif step is 3:
                if monster.spawnPosition[0]-(monster.position[0]-1) > 5:
                    print monster.position, " vs ", monster.spawnPosition
                    print "Stop by west"
                    continue
            
            def success(result):
                monster.lastStep = time.time()
            d = monster.move(step, spectators)
            d.addCallback(success)
            d.addErrback(game.engine.ignore)
            return True
        return False
        
brains = {}
brains["default"] = MonsterBrain()
def genMonster(name, look, description="", brain="default"):
    # First build the common creature data
    data = {"lookhead":0, "lookfeet":0, "lookbody":0, "looklegs":0}

    data["looktype"] = look[0]
    data["corpse"] = look[1]
    data["name"] = name
    # Then monster only data
    monsters[name] = MonsterBase(data, brains[brain], None)

    return monsters[name]

def getMonster(name):
    if name in monsters:
        return monsters[name]
    else:
        return None