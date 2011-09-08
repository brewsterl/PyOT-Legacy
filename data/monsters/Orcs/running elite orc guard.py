import game.monster

running_elite_orc_guard = game.monster.genMonster("Running Elite Orc Guard", (7, 5979), "a running elite orc guard")
running_elite_orc_guard.setHealth(1)
running_elite_orc_guard.bloodType(color="blood")
running_elite_orc_guard.setDefense(-1)
running_elite_orc_guard.setExperience(0)
running_elite_orc_guard.setSpeed(200)
running_elite_orc_guard.setBehavior(summonable=0, hostile=0, illusionable=0, convinceable=0, pushable=0, pushItems=1, pushCreatures=1, targetDistance=1, runOnHealth=1)
running_elite_orc_guard.walkAround(energy=0, fire=0, poison=0)
running_elite_orc_guard.setImmunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)