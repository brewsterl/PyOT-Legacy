if config.regenerationTresshold > 0:
    def regenerator(player):
        if player.data['health'] < config.regenerationTresshold:
            player.setHealth(config.regenerationTresshold)

    @register('hit', 'player')
    def regen(creature, damage, **k):
        if (creature.data['health']-damage < config.regenerationTresshold \
           and not creature.hasCondition(CONDITION_INFIGHT) and not (creature.extraIcons & CONDITION_PROTECTIONZONE)):
            callLater(config.regenerationDelay, regenerator, creature)