import game.monster

ice_witch = game.monster.genMonster("Ice Witch", (149, 6081), "an ice witch")
ice_witch.setOutfit(0, 47, 105, 105)
ice_witch.setHealth(650)
ice_witch.bloodType(color="blood")
ice_witch.setDefense(armor=15, fire=0.5, earth=1, energy=1, ice=0, holy=1, death=1, physical=1, drown=1)
ice_witch.setExperience(580)
ice_witch.setSpeed(188)
ice_witch.setBehavior(summonable=0, hostile=1, illusionable=0, convinceable=0, pushable=0, pushItems=1, pushCreatures=1, targetDistance=4, runOnHealth=0)
ice_witch.walkAround(energy=1, fire=1, poison=1)
ice_witch.setImmunity(paralyze=1, invisible=1, lifedrain=1, drunk=0)
ice_witch.voices("So you think you are cool?", "I hope it is not too cold for you! HeHeHe.", "Freeze!")
ice_witch.regMelee(60)