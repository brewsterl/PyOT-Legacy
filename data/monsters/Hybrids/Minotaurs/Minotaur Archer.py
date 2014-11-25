minotaur_archer = genMonster("Minotaur Archer", 24, 5982)
minotaur_archer.health(100)
minotaur_archer.type("blood")
minotaur_archer.defense(armor=7, fire=0.8, earth=1, energy=1, ice=1.1, holy=0.9, death=1.05, physical=1, drown=1)
minotaur_archer.experience(65)
minotaur_archer.speed(170)
minotaur_archer.behavior(summonable=390, hostile=True, illusionable=True, convinceable=390, pushable=True, pushItems=False, pushCreatures=True, targetDistance=4, runOnHealth=10)
minotaur_archer.walkAround(energy=0, fire=0, poison=0)
minotaur_archer.immunity(paralyze=0, invisible=0, lifedrain=0, drunk=0)
minotaur_archer.voices("Ruan Wihmpy!", "Kaplar!")
minotaur_archer.melee(25)
minotaur_archer.distance(80, ANIMATION_BOLT, chance(21))
minotaur_archer.loot( ("meat", 5.25), ("piercing bolt", 28.5, 4), ("piece of archer armor", 7.75), (2148, 100, 30), ("broken crossbow", 15.0), ("bolt", 100, 20), ("minotaur leather", 1.5, 3), ("minotaur horn", 1.75, 2), ("brass armor", 0.5), ("crossbow", 1.25), ("scale armor", 0.25) )