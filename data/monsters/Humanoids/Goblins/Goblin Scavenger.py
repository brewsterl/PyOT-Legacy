goblin_scavenger = genMonster("Goblin Scavenger", 297, 6002)
goblin_scavenger.health(60, healthmax=60)
goblin_scavenger.type("blood")
goblin_scavenger.defense(armor=7, fire=1, earth=1.1, energy=0.8, ice=1, holy=0.8, death=1.1, physical=1, drown=1)
goblin_scavenger.experience(37)
goblin_scavenger.speed(220)
goblin_scavenger.behavior(summonable=0, hostile=True, illusionable=True, convinceable=310, pushable=True, pushItems=False, pushCreatures=False, targetDistance=1, runOnHealth=12)
goblin_scavenger.walkAround(energy=1, fire=1, poison=1)
goblin_scavenger.immunity(paralyze=1, invisible=0, lifedrain=0, drunk=0)
goblin_scavenger.voices("Shiny, shiny!", "You mean!", "All mine!", "Uhh!", "Gimme gimme!")
goblin_scavenger.melee(15)
goblin_scavenger.distance(30, ANIMATION_SPEAR, chance(21))
goblin_scavenger.loot( ("leather helmet", 11.25), ("small axe", 9.5), ("bone", 10.75), (2235, 6.25), ("leather armor", 10.25), ("short sword", 10.25), ("dagger", 18.75), ("small stone", 37.0, 2), ("bone club", 6.25), (2148, 100, 9), ("fish", 12.0) )