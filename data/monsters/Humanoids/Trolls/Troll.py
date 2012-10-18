troll = genMonster("Troll", (15, 5960), "a troll")
troll.setHealth(50)
troll.bloodType(color="blood")
troll.setDefense(armor=6, fire=1, earth=1.1, energy=0.85, ice=1, holy=0.9, death=1.1, physical=1, drown=1)
troll.setExperience(20)
troll.setSpeed(126)
troll.setBehavior(summonable=290, hostile=1, illusionable=1, convinceable=290, pushable=1, pushItems=0, pushCreatures=0, targetDistance=1, runOnHealth=15)
troll.walkAround(energy=1, fire=1, poison=1)
troll.setImmunity(paralyze=0, invisible=0, lifedrain=0, drunk=0)
troll.voices("Hmmm, bugs", "Hmmm, dogs", "Grrr", "Groar", "Gruntz!")
troll.regMelee(15)
troll.loot( ("spear", 13.5), ("rope", 8.75), (2148, 100, 12), ("meat", 15.25), ("wooden shield", 10.5), ("hand axe", 17.25), ("leather helmet", 12.0), ("leather boots", 10.0), ("studded club", 4.75), ("bunch of troll hair", 0.75), ("silver amulet", 0.0025) )