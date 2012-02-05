quara_mantassin = game.monster.genMonster("Quara Mantassin", (72, 6064), "a quara mantassin")
quara_mantassin.setHealth(800)
quara_mantassin.bloodType(color="blood")
quara_mantassin.setDefense(armor=17, fire=0, earth=1.1, energy=1.25, ice=0, holy=1, death=1, physical=1, drown=0)
quara_mantassin.setExperience(400)
quara_mantassin.setSpeed(520)
quara_mantassin.setBehavior(summonable=0, hostile=1, illusionable=0, convinceable=480, pushable=0, pushItems=1, pushCreatures=0, targetDistance=1, runOnHealth=40)
quara_mantassin.walkAround(energy=1, fire=0, poison=1)
quara_mantassin.setImmunity(paralyze=1, invisible=0, lifedrain=0, drunk=1)
quara_mantassin.voices("Shrrrr", "Zuerk Pachak!")
quara_mantassin.loot( ("halberd", 4.0), (2148, 100, 129), ("blue robe", 0.25), ("stealth ring", 1.0), ("fish fin", 0.5, 3), ("two handed sword", 1.0), ("cape", 1.0), ("small sapphire", 1.25), ("shrimp", 4.75), ("mantassin tail", 9.5), ("strange helmet", 0.0025) )


quara_mantassin.regMelee(140)
quara_mantassin.regSelfSpell("Haste", 360, 360, length=8, check=game.monster.chance(9)) #strength time?
#quara_mantassin.regSelfSpell("Invisible", 360, 360, length=8, check=game.monster.chance(9))