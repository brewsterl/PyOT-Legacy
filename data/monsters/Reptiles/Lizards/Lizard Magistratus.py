#mostly unknown
lizard_magistratus = game.monster.genMonster("Lizard Magistratus", (115, 6041), "a lizard magistratus")
lizard_magistratus.setHealth(8000)
lizard_magistratus.bloodType(color="blood")
lizard_magistratus.setDefense(armor=27, fire=0.15, earth=0, energy=1, ice=1, holy=1, death=1, physical=1, drown=1)
lizard_magistratus.setExperience(200)
lizard_magistratus.setSpeed(210)
lizard_magistratus.setBehavior(summonable=0, hostile=1, illusionable=0, convinceable=0, pushable=0, pushItems=1, pushCreatures=1, targetDistance=4, runOnHealth=0)
lizard_magistratus.walkAround(energy=0, fire=0, poison=0)
lizard_magistratus.setImmunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
lizard_magistratus.voices("Shhhhhh")
lizard_magistratus.regMelee(60)
#lizard_magistratus.loot()