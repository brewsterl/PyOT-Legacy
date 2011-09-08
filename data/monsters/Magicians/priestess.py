import game.monster

priestess = game.monster.genMonster("Priestess", (58, 6081), "a priestess")
priestess.setHealth(390)
priestess.bloodType(color="blood")
priestess.setDefense(armor=20, fire=0.6, earth=0.3, energy=1, ice=1, holy=1.1, death=0.9, physical=1.1, drown=1)
priestess.setExperience(420)
priestess.setSpeed(220)
priestess.setBehavior(summonable=0, hostile=1, illusionable=1, convinceable=0, pushable=0, pushItems=1, pushCreatures=1, targetDistance=4, runOnHealth=0)
priestess.walkAround(energy=1, fire=1, poison=1)
priestess.setImmunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
priestess.voices("Your energy is mine.", "Now your life is come to the end, hahahaha!", "Throw the soul on the altar!")
priestess.regMelee(75)