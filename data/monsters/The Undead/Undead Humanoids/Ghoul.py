ghoul = genMonster("Ghoul", 18, 5976)
ghoul.health(100)
ghoul.type("blood")
ghoul.defense(armor=9, fire=1, earth=0.8, energy=0.7, ice=0.9, holy=1.25, death=0, physical=1, drown=0)
ghoul.experience(85)
ghoul.speed(144)
ghoul.behavior(summonable=450, hostile=True, illusionable=True, convinceable=450, pushable=False, pushItems=True, pushCreatures=True, targetDistance=1, runOnHealth=0)
ghoul.walkAround(energy=1, fire=1, poison=1)
ghoul.immunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
ghoul.melee(70)
ghoul.loot( (3976, 14.5, 2), ("ghoul snack", 5.25), ("rotten piece of cloth", 15.5), ("torch", 4.5), (2148, 100, 30), ("pile of grave earth", 1.0), ("brown piece of cloth", 1.25, 3), ("scale armor", 0.75), ("skull", 0.25), ("viking helmet", 1.0), ("life ring", 0.25) )