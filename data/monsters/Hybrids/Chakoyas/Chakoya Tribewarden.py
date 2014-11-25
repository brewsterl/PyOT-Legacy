chakoya_tribewarden = genMonster("Chakoya Tribewarden", 258, 7320)#261? wrong looktype?
chakoya_tribewarden.health(68, healthmax=68)
chakoya_tribewarden.type("blood")
chakoya_tribewarden.defense(armor=9, fire=0.75, earth=1, energy=1.15, ice=0, holy=0.9, death=1.05, physical=1, drown=1)
chakoya_tribewarden.experience(40)
chakoya_tribewarden.speed(270)
chakoya_tribewarden.behavior(summonable=0, hostile=True, illusionable=False, convinceable=305, pushable=False, pushItems=False, pushCreatures=False, targetDistance=1, runOnHealth=0)
chakoya_tribewarden.walkAround(energy=1, fire=1, poison=1)
chakoya_tribewarden.immunity(paralyze=0, invisible=0, lifedrain=0, drunk=0)
chakoya_tribewarden.voices("Quisavu tukavi!", "Si siyoqua jamjam!", "Achuq! jinuma!", "Si ji jusipa!")
chakoya_tribewarden.melee(30)
chakoya_tribewarden.loot( (2148, 100, 20), ("fish", 20.0), ("rainbow trout", 0.25), ("short sword", 3.75), ("bone shield", 1.0), ("green perch", 0.25), ("mammoth whopper", 0.25), ("northern pike", 0.0025) )