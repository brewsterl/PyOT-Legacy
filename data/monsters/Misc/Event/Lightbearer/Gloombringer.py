#largely unknown
gloombringer = genMonster("Gloombringer", (12, 5980), "a gloombringer")
gloombringer.setHealth(10000)
gloombringer.bloodType("blood")
gloombringer.setDefense(armor=1, fire=1, earth=1, energy=1, ice=1, holy=1, death=1, physical=1, drown=1)
gloombringer.setExperience(0)
gloombringer.setSpeed(300)
gloombringer.setBehavior(summonable=0, hostile=1, illusionable=0, convinceable=0, pushable=0, pushItems=1, pushCreatures=1, targetDistance=1, runOnHealth=0)
gloombringer.walkAround(energy=0, fire=0, poison=0)
gloombringer.setImmunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
gloombringer.regMelee(3000)