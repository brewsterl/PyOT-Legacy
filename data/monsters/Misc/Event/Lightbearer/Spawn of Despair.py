#largely unknown
spawn_of_despair = genMonster("Spawn of Despair", (322, 9923), "a spawn of despair")
spawn_of_despair.setHealth(10000)
spawn_of_despair.bloodType("blood")
spawn_of_despair.setDefense(armor=10, fire=1, earth=1, energy=1, ice=1.1, holy=1.1, death=1.1, physical=1, drown=1)
spawn_of_despair.setExperience(100)
spawn_of_despair.setSpeed(200)
spawn_of_despair.setBehavior(summonable=0, hostile=1, illusionable=0, convinceable=0, pushable=0, pushItems=1, pushCreatures=1, targetDistance=1, runOnHealth=0)
spawn_of_despair.walkAround(energy=0, fire=0, poison=0)
spawn_of_despair.setImmunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
spawn_of_despair.voices("Tibia will suffer and writhe today!", "Times of darkness are at hand", "The light weakens! The darkness grows stronger!", "YOU CALLED US! HERE WE ARE!", "The world will end today", "HRAAAAAAAAAAH", "OUR DAY HAS COME!", "HIDE YOU WEAKLINGS!", "Give it up. You fragile beings cannot have hope to defeat us demons.")
spawn_of_despair.regMelee(500)