import game.monster

death_blob = game.monster.genMonster("Death Blob", (315, 9960), "a death blob")
death_blob.setHealth(320)
death_blob.bloodType(color="undead")
death_blob.setDefense(armor=10, fire=1.1, earth=0, energy=1.1, ice=0.9, holy=1.1, death=0, physical=0.8, drown=1)
death_blob.setExperience(300)
death_blob.setSpeed(230)
death_blob.setBehavior(summonable=0, hostile=1, illusionable=0, convinceable=0, pushable=0, pushItems=1, pushCreatures=0, targetDistance=1, runOnHealth=0)
death_blob.walkAround(energy=1, fire=1, poison=0)
death_blob.setImmunity(paralyze=0, invisible=0, lifedrain=1, drunk=1)
death_blob.regMelee(100)