LIGHTLEVEL_NONE = 0
LIGHTLEVEL_TORCH = 7
LIGHTLEVEL_FULL = 27
LIGHTLEVEL_WORLD = 255

LIGHTCOLOR_NONE = 0
LIGHTCOLOR_DEFAULT = 206 # Orange
LIGHTCOLOR_WHITE = 215

SLOT_WHEREEVER = 0
SLOT_FIRST = 1
SLOT_HEAD = SLOT_FIRST
SLOT_NECKLACE = 2
SLOT_BACKPACK = 3
SLOT_ARMOR = 4
SLOT_RIGHT = 5
SLOT_LEFT = 6
SLOT_LEGS = 7
SLOT_FEET = 8
SLOT_RING = 9
SLOT_AMMO = 10
SLOT_DEPOT = 11
SLOT_LAST = SLOT_DEPOT
SLOT_HAND = 12
SLOT_TWO_HAND = 12

# Chat
MSG_NONE			= 0x00
MSG_SPEAK_SAY			= 0x01
MSG_SPEAK_WHISPER		= 0x02
MSG_SPEAK_YELL			= 0x03
MSG_PRIVATE_FROM		= 0x04
MSG_PRIVATE_TO			= 0x05
MSG_CHANNEL_MANAGEMENT		= 0x06
MSG_CHANNEL			= 0x07
MSG_CHANNEL_HIGHLIGHT		= 0x08
MSG_SPEAK_SPELL			= 0x09
MSG_NPC_FROM			= 0x0A
MSG_NPC_TO			= 0x0B
MSG_GAMEMASTER_BROADCAST	= 0x0C
MSG_GAMEMASTER_CHANNEL		= 0x0D
MSG_GAMEMASTER_PRIVATE_FROM	= 0x0E
MSG_GAMEMASTER_PRIVATE_TO	= 0x0F
MSG_SPEAK_MONSTER_SAY		= 0x22
MSG_SPEAK_MONSTER_YELL		= 0x23
MSG_SPEAK_FIRST			= MSG_SPEAK_SAY
MSG_SPEAK_LAST			= MSG_GAMEMASTER_PRIVATE_FROM
MSG_SPEAK_MONSTER_FIRST		= MSG_SPEAK_MONSTER_SAY
MSG_SPEAK_MONSTER_LAST		= MSG_SPEAK_MONSTER_YELL
MSG_STATUS_CONSOLE_RED		= 0x0C # Red message in the console
MSG_STATUS_DEFAULT		= 0x10 # White message at the bottom of the game window and in the console
MSG_STATUS_WARNING		= 0x11 # Red message in game window and in the console
MSG_EVENT_ADVANCE		= 0x12 # White message in game window and in the console
MSG_STATUS_SMALL		= 0x13 # White message at the bottom of the game window"
MSG_INFO_DESCR			= 0x14 # Green message in game window and in the console
MSG_DAMAGE_DEALT		= 0x15
MSG_DAMAGE_RECEIVED		= 0x16
MSG_HEALED			= 0x17
MSG_EXPERIENCE			= 0x18
MSG_DAMAGE_OTHERS		= 0x19
MSG_HEALED_OTHERS		= 0x1A
MSG_EXPERIENCE_OTHERS		= 0x1B
MSG_EVENT_DEFAULT		= 0x1C # White message at the bottom of the game window and in the console
MSG_LOOT			= 0x1D
MSG_TRADE_NPC			= 0x1E
MSG_CHANNEL_GUILD		= 0x1F # SPEAK_CHANNEL_W(?) guild messages.
MSG_PARTY_MANAGEMENT		= 0x20
MSG_PARTY			= 0x21
MSG_EVENT_ORANGE		= 0x22 # Orange message in the console
MSG_STATUS_CONSOLE_ORANGE	= 0x23 # Orange message in the console
MSG_REPORT 			= 0x24
MSG_HOTKEY_USE			= 0x25
MSG_TUTORIAL_HINT		= 0x26
MSG_STATUS_CONSOLE_BLUE		= 0xFF


# Fluids
FLUID_EMPTY                     = 0x00
FLUID_BLUE                      = 0x01
FLUID_RED                       = 0x02
FLUID_BROWN                     = 0x03
FLUID_GREEN                     = 0x04
FLUID_YELLOW                    = 0x05
FLUID_WHITE                     = 0x06
FLUID_PURPLE                    = 0x07

FLUID_NONE                      = FLUID_EMPTY,
FLUID_WATER                     = FLUID_BLUE,
FLUID_BLOOD                     = FLUID_RED,
FLUID_BEER                      = FLUID_BROWN,
FLUID_SLIME                     = FLUID_GREEN,
FLUID_LEMONADE                  = FLUID_YELLOW,
FLUID_MILK                      = FLUID_WHITE,
FLUID_MANA                      = FLUID_PURPLE,

FLUID_LIFE                      = FLUID_RED + 8,
FLUID_OIL                       = FLUID_BROWN + 8,
FLUID_URINE                     = FLUID_YELLOW + 8,
FLUID_COCONUTMILK               = FLUID_WHITE + 8,
FLUID_WINE                      = FLUID_PURPLE + 8,

FLUID_MUD                       = FLUID_BROWN + 16,
FLUID_FRUITJUICE                = FLUID_YELLOW + 16,

FLUID_LAVA                      = FLUID_RED + 24,
FLUID_RUM                       = FLUID_BROWN + 24,
FLUID_SWAMP                     = FLUID_GREEN + 24,

FLUID_TEA                       = FLUID_BROWN + 32,
FLUID_MEAD                      = FLUID_BROWN + 40

reversFluids = [FLUID_EMPTY, FLUID_WATER, FLUID_MANA, FLUID_BEER, FLUID_EMPTY, FLUID_BLOOD, FLUID_SLIME, FLUID_EMPTY, FLUID_LEMONADE, FLUID_MILK]

# Floorchange
FLOORCHANGE_DOWN                = 0x00
FLOORCHANGE_UP                  = 0x01
