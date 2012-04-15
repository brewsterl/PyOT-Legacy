lizard_templar = game.monster.genMonster(_("Lizard Templar"), (113, 4251), _("a lizard templar"))
lizard_templar.setHealth(410, healthmax=410)
lizard_templar.bloodType(color="blood")
lizard_templar.setDefense(armor=29, fire=1.1, earth=0, energy=0.8, ice=0.9, holy=1, death=1, physical=1, drown=1)
lizard_templar.setExperience(155)
lizard_templar.setSpeed(210)
lizard_templar.setBehavior(summonable=0, hostile=1, illusionable=1, convinceable=0, pushable=0, pushItems=1, pushCreatures=0, targetDistance=1, runOnHealth=0)
lizard_templar.walkAround(energy=1, fire=1, poison=0)
lizard_templar.setImmunity(paralyze=1, invisible=0, lifedrain=1, drunk=1)
lizard_templar.voices("Hissss!")
lizard_templar.regMelee(70)
lizard_templar.loot( (2148, 100, 60), ("lizard leather", 0.75), ("sword", 5.25), ("steel helmet", 2.0), ("short sword", 10.0), ("templar scytheblade", 0.5), ("health potion", 1.0), ("morning star", 2.5), ("lizard scale", 1.0, 3), ("plate armor", 1.0), ("small emerald", 0.25) )