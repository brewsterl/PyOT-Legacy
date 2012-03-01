draken_abomination = game.monster.genMonster("Draken Abomination", (357, 12623), "a draken abomination")
draken_abomination.setHealth(6250, healthmax=6250)
draken_abomination.bloodType(color="blood")
draken_abomination.setDefense(armor=46, fire=0, earth=0, energy=1.05, ice=0.95, holy=1.05, death=0, physical=1, drown=1)
draken_abomination.setExperience(3800)
draken_abomination.setSpeed(220)
draken_abomination.setBehavior(summonable=0, hostile=1, illusionable=0, convinceable=0, pushable=0, pushItems=1, pushCreatures=1, targetDistance=1, runOnHealth=0)
draken_abomination.walkAround(energy=0, fire=0, poison=0)
draken_abomination.setImmunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
draken_abomination.summon("Death Blobs", 10)
draken_abomination.maxSummons(2)
draken_abomination.voices("Ugggh!", "Gll")
draken_abomination.regMelee(300)
draken_abomination.loot( ("small topaz", 7.0, 4), ("ultimate health potion", 22.25, 3), ("meat", 48.75, 4), ("platinum coin", 100, 8), (2148, 100, 195), ("scale of corruption", 9.0), ("eye of corruption", 13.25), ("tail of corruption", 5.5), ("terra hood", 8.5), ("great spirit potion", 10.25, 3), ("zaoan legs", 1.25), ("great mana potion", 17.5, 3), ("draken boots", 1.0), ("zaoan helmet", 0.5), ("wand of voodoo", 1.5), ("zaoan armor", 1.0) )