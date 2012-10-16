earth_elemental = genMonster("Earth Elemental", (301, 8933), "a earth elemental")
earth_elemental.setHealth(650)
earth_elemental.bloodType(color="undead")
earth_elemental.setDefense(armor=58, fire=1.25, earth=0, energy=0, ice=0.85, holy=0.5, death=0.6, physical=0.7, drown=1)
earth_elemental.setExperience(450)
earth_elemental.setSpeed(330)
earth_elemental.setBehavior(summonable=0, hostile=1, illusionable=1, convinceable=0, pushable=0, pushItems=1, pushCreatures=1, targetDistance=1, runOnHealth=0)
earth_elemental.walkAround(energy=0, fire=1, poison=0)
earth_elemental.setImmunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
earth_elemental.regMelee(120)
earth_elemental.loot( (2148, 100, 100), ("small stone", 15.0, 2), ("earth arrow", 100, 27), ("blank rune", 10.0), ("lump of earth", 10.0), ("rusty armor", 5.0) )