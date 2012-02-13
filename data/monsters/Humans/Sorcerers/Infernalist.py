infernalist = game.monster.genMonster("Infernalist", (130, 6080), "a infernalist")
infernalist.setOutfit(78, 76, 94, 115) #needs 2 addons
infernalist.setHealth(3650, healthmax=3650)
infernalist.bloodType(color="blood")
infernalist.setDefense(armor=37, fire=0, earth=0.05, energy=0, ice=1.05, holy=0.8, death=0.9, physical=1.05, drown=1)
infernalist.setExperience(4000)
infernalist.setSpeed(260)
infernalist.setBehavior(summonable=0, hostile=1, illusionable=0, convinceable=0, pushable=0, pushItems=1, pushCreatures=1, targetDistance=4, runOnHealth=1150)
infernalist.walkAround(energy=0, fire=0, poison=0)
infernalist.setImmunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
infernalist.summon("fire elemental", 10)
infernalist.maxSummons(1)
infernalist.voices("Nothing will remain but your scorched bones!", "Some like it hot!", "It's cooking time!", "Feel the heat of battle!")
infernalist.regMelee(100)
infernalist.loot( ("raspberry", 24.0, 5), (2148, 100, 147), ("great mana potion", 19.5), ("great health potion", 20.25), ("skull staff", 6.5), ("red tome", 0.25), (7760, 4.5), ("energy ring", 2.0), ("black skull", 0.0025), ("red piece of cloth", 0.75, 3), ("royal tapestry", 0.5), ("magic sulphur", 0.5), ("magma boots", 0.0025), ("gold ingot", 0.25), ("spellbook of mind control", 0.25) )