war_golem = genMonster("War Golem", 326, 10005)
war_golem.health(4300)
war_golem.type("blood")
war_golem.defense(armor=39, fire=0.85, earth=0.5, energy=0.95, ice=0.3, holy=0.5, death=0.2, physical=0.9, drown=1)
war_golem.experience(2750)
war_golem.speed(280)
war_golem.behavior(summonable=0, hostile=True, illusionable=False, convinceable=0, pushable=False, pushItems=True, pushCreatures=True, targetDistance=1, runOnHealth=0)
war_golem.walkAround(energy=0, fire=0, poison=0)
war_golem.immunity(paralyze=1, invisible=1, lifedrain=0, drunk=0)
war_golem.voices("Azerus barada nikto!", "Klonk klonk klonk", "Engaging Enemy!", "Threat level processed.", "Charging weapon systems!", "Auto repair in progress.", "The battle is joined!", "Termination initialized!", "Rrrtttarrrttarrrtta", "Eliminated")
war_golem.melee(480)
war_golem.loot( ("crystal pedestal", 1.0), ("rusty armor", 3.0), ("two handed sword", 5.0), ("morning star", 7.75), ("battle shield", 5.0), ("ultimate health potion", 10.0), ("dwarven ring", 1.25), ("great mana potion", 8.75), ("nail", 14.25, 5), (2148, 100, 263), ("crystal of power", 0.0025), ("steel boots", 0.5), ("life crystal", 1.0), ("bonebreaker", 0.75), ("berserk potion", 1.0), ("berserker", 0.0025), ("club ring", 1.0), ("epee", 7.0), ("war crystal", 8.0), ("iron ore", 2.25, 3), ("plate shield", 8.25), ("jade hammer", 0.25), ("lightning boots", 0.0025), ("tin key", 0.0025) )