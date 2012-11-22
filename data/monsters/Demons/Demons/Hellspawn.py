hellspawn = genMonster("Hellspawn", (322, 9923), "a hellspawn")
hellspawn.setHealth(3500)
hellspawn.bloodType("blood")
hellspawn.setDefense(armor=68, fire=0.6, earth=0.2, energy=0.9, ice=1.1, holy=0.7, death=1.05, physical=0.9, drown=1)
hellspawn.setExperience(2550)
hellspawn.setSpeed(300)
hellspawn.setBehavior(summonable=0, hostile=1, illusionable=0, convinceable=0, pushable=0, pushItems=1, pushCreatures=1, targetDistance=1, runOnHealth=0)
hellspawn.walkAround(energy=1, fire=0, poison=0)
hellspawn.setImmunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
hellspawn.voices("Your fragile bones are like toothpicks to me.", "You little weasel will not live to see another day.", "I'm just a messenger of what's yet to come.", "HRAAAAAAAAAAAAAAAARRRR!", "I'm taking you down with me!")
hellspawn.regMelee(350)#or more
hellspawn.loot( ("warrior helmet", 2.0), ("knight legs", 3.25), ("rusty armor", 3.25, 2), ("dracoyle statue", 0.0025), ("spiked squelcher", 0.75), ("berserk potion", 1.0), ("ultimate health potion", 10.0), ("demonic essence", 10.25, 3), ("assassin star", 15.5, 2), ("red mushroom", 11.75, 2), ("morning star", 9.75), ("small topaz", 12.25, 3), ("hellspawn tail", 20.0), ("great health potion", 40.0), ("battle shield", 10.0), (2148, 100, 234), ("black skull", 0.25), ("onyx flail", 0.0025) )