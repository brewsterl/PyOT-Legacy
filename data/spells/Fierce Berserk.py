instant = spell.Spell("Fierce Berserk", "exori gran", icon=105, group=ATTACK_GROUP)
instant.require(mana=340, level=90, maglevel=0, learned=0, vocations=(4, 8))
instant.cooldowns(6, 2)
instant.area(AREA_SQUARE)
instant.targetEffect(callback=spell.damage(3.184, 5.59, 13, 27, PHYSICAL)) #unknown (x, x, 13, 27)
instant.effects() # TODO