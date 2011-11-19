goblin_assassin = game.monster.genMonster("Goblin Assassin", (296, 6002), "a goblin assassin")
goblin_assassin.setHealth(75, healthmax=75)
goblin_assassin.bloodType(color="blood")
goblin_assassin.setDefense(armor=11, fire=1, earth=1.1, energy=0.8, ice=1, holy=0.8, death=1.1, physical=1, drown=1)
goblin_assassin.setExperience(52)
goblin_assassin.setSpeed(220)
goblin_assassin.setBehavior(summonable=0, hostile=1, illusionable=1, convinceable=360, pushable=1, pushItems=0, pushCreatures=0, targetDistance=1, runOnHealth=20)
goblin_assassin.walkAround(energy=1, fire=1, poison=1)
goblin_assassin.setImmunity(paralyze=0, invisible=0, lifedrain=0, drunk=0)
goblin_assassin.voices("Goblin Powahhh!", "Me kill you!", "Me green menace!", "Gobabunga!", "Gooobliiiins!")
goblin_assassin.regMelee(15)
goblin_assassin.loot( ("bone club", 5.0), ("leather armor", 7.75), ("small axe", 12.25), (2235, 6.75), ("leather helmet", 11.0), (2148, 100, 9), ("dagger", 18.75), ("small stone", 21.5, 3), ("fish", 14.5), ("bone", 10.5), ("short sword", 9.0) )