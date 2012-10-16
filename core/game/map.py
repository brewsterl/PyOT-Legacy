from game.item import Item
import game.item
from twisted.internet import threads, reactor
from twisted.python import log
import scriptsystem
from collections import deque
import config
import game.enum
import time
import io
import struct
import sys
import itertools
import gc

##### Position class ####
def __uid():
    idsTaken = 1
    while True:
        idsTaken += 1
        yield idsTaken
instanceId = __uid().next
        
def getTile(pos):
    x,y,z,instanceId = pos.x, pos.y, pos.z, pos.instanceId
    iX = x >> 5
    iY = y >> 5
    pX = x & 31
    pY = y & 31

    try:
        area = knownMap[instanceId]
    except KeyError:
        knownMap[instanceId] = {}
        area = knownMap[instanceId]
        
    sectorSum = (iX << 15) + iY
    try:
        return area[sectorSum][z][pX][pY]
    except KeyError:
        if loadTiles(x, y, instanceId):
            try:
                return area[sectorSum][z][pX][pY]
            except:
                return None
    except:
        return None

def getTileConst(x,y,z,instanceId):
    iX = x >> 5
    iY = y >> 5
    pX = x & 31
    pY = y & 31

    try:
        area = knownMap[instanceId]
    except KeyError:
        knownMap[instanceId] = {}
        area = knownMap[instanceId]
        
    sectorSum = (iX << 15) + iY
    try:
        return area[sectorSum][z][pX][pY]
    except KeyError:
        if loadTiles(x, y, instanceId):
            try:
                return area[sectorSum][z][pX][pY]
            except:
                return None
    except:
        return None
        
def getHouseId(pos):
    try:
        return getTile(pos).houseId
    except:
        return False
        
def placeCreature(creature, pos):
    try:
        return getTile(pos).placeCreature(creature)
    except:
        return False
        
def removeCreature(creature, pos):
    try:
        return getTile(pos).removeCreature(creature)
    except:
        return False  

DEFAULT_BASE = ''
def newInstance(base=None):
    instance = instanceId()
    if base:
        instances[instance] = base + '/'
    else:
        instances[instance] = DEFAULT_BASE
        
    return instance
        
PACK_ITEMS = 0 # top items
PACK_CREATURES = 8
PACK_FLAGS = 16

class Tile(object):
    __slots__ = ('things', 'countNflags')
    def __init__(self, items, flags=0, count=0):
        self.things = items
        
        if not count:
            self.countNflags = 1
            if len(items) > 1:
                for item in self.things:
                    if item.ontop:
                        self.countNflags += 1
  
        else:
            self.countNflags = count

        if flags:
            self._modpack(PACK_FLAGS, flags)

    def _depack(self, level):
        return (self.countNflags >> level) & 255
        
    def _modpack(self, level, mod):
        self.countNflags += mod << level

    def getCreatureCount(self):
        return self._depack(PACK_CREATURES)
    
    def getItemCount(self):
        return len(self.things) - self._depack(PACK_CREATURES)
        
    def getFlags(self):
        return self._depack(PACK_FLAGS)
        
    def setFlag(self, flag):
        if not self.getFlags() & flag:
            self._modpack(PACK_FLAGS, flag)

    def unsetFlag(self, flag):
        if self.getFlags() & flag:
            self._modpack(PACK_FLAGS, -flag)
            
    def placeCreature(self, creature):
        pos = self._depack(PACK_ITEMS) + self._depack(PACK_CREATURES)
        self.things.insert(pos, creature)
        self._modpack(PACK_CREATURES, 1)
        if pos > 9:
            print self.things
            print pos, self.countNflags
            raise Exception("Item position > 9! Likely we need to deal with this ")
        return pos
        
    def removeCreature(self,creature):
        self.things.remove(creature)
        self._modpack(PACK_CREATURES, -1)
        
    def placeItem(self, item):
        if item.ontop:
            pos = self._depack(PACK_ITEMS)
            self._modpack(PACK_ITEMS, 1)
        else:
            pos = self._depack(PACK_ITEMS) + self._depack(PACK_CREATURES)
        self.things.insert(pos, item)
        if pos > 9:
            print self.things
            print pos, self.countNflags
            raise Exception("Item position > 9! Likely we need to deal with this ")
        return pos
    
    def placeItemEnd(self, item):
        self.things.append(item)
        return len(self.things)-1

    def ground(self):
        return self.things[0]
        
    def bottomItems(self):
        x = self._depack(PACK_ITEMS) + self._depack(PACK_CREATURES)
        for n in xrange(x, len(self.things)):
            yield self.things[n]
        
    def topItems(self):
        for n in xrange(self._depack(PACK_ITEMS)):
            
            try:
                yield self.things[n]
            except:
                print "XXX: Hack applied"
                self._modpack(PACK_ITEMS, -1)
                return
            
    def getItems(self):
        return itertools.chain(self.topItems(), self.bottomItems())
 
    def creatures(self):
        cc = self._depack(PACK_ITEMS)
        cd = self._depack(PACK_CREATURES)
        for n in xrange(cc, cc + cd):
            try:
                yield self.things[n]
            except:
                return
                
    def hasCreatures(self):
        return self._depack(PACK_CREATURES)
        
    def topCreature(self):
        cd = self._depack(PACK_CREATURES)
        if cd:
            cc = self._depack(PACK_ITEMS)
            return self.things[cc]

    def removeItem(self, item):
        item.stopDecay()
        self.things.remove(item)
        if item.ontop:
            self._modpack(PACK_ITEMS, -1)

    def removeItemWithId(self, itemId):
        for i in self.getItems():
            if i.itemId == itemId:
                self.removeItem(i)
                
        
    def getThing(self, stackpos):
        try:
            return self.things[stackpos]
        except:
            return None
    
    def setThing(self, stackpos, item):
        self.things[stackpos] = item
        
    def findItem(self, sid):
        for x in self.bottomItems():
            if x.itemId == sid:
                return x

    def findStackpos(self, thing):
        return self.things.index(thing)
        
    def findClientItem(self, cid, stackpos=None):
        for x in self.bottomItems():
            if x.cid == cid:
                if stackpos:
                    return (self.things.index(x), x)
                return x
                
    def findCreatureStackpos(self, creature):
        return self.things.index(creature)

    def __getstate__(self):
        return (self.things, self.countNflags)
    
    def __setstate__(self, saved):
        self.things = saved[0]
        self.countNflags = saved[1]
        

class HouseTile(Tile):
    __slots__ = ('houseId', 'position')
    def __getstate__(self):
        
        # Remove all non-loaded things for the sake of the cache. 
        items = []
        cf = self.getFlags()
        for i in self.things:
            if i.fromMap:
                items.append(i)
                if i.ontop:
                    cf += 1
        
        return (items, cf, self.houseId, self.position)
    
    def __setstate__(self, saved):
        self.things = saved[0]      
        self.countNflags = saved[1]  
        self.houseId = saved[2]
        self.position = saved[3]
        
        if self.houseId in houseTiles:
            houseTiles[self.houseId].append(self)
        else:
            houseTiles[self.houseId] = [self]
        
        check = True    
        for i in self.things:
            if i.hasAction("houseDoor"):
                if check and self.houseId in houseDoors:
                    houseDoors[self.houseId].append(self.position)
                    check = False
                else:
                    houseDoors[self.houseId] = [self.position]

        try:
            for item in game.house.houseData[self.houseId].data["items"][self.position]:
                if item and item.itemId:
                    self.placeItem(item)
        except KeyError:
            pass
    

import data.map.info as mapInfo
dummyItems = {} 

knownMap = {None: {}} # InstanceId -> {z: [x -> [y]]}

instances = {None: ''}

houseTiles = {}

houseDoors = {}

if config.stackTiles:
    dummyTiles = {}
    
def loadTiles(x,y, instanceId):
    if x > mapInfo.height or y > mapInfo.width or x < 0 or y < 0:
        return None
    
    return load(x // mapInfo.sectorSize[0], y // mapInfo.sectorSize[1], instanceId)

### Start New Map Format ###

attributeIds = ('actions', 'count', 'solid','blockprojectile','blockpath','usable','pickable','movable','stackable','ontop','hangable','rotatable','animation', 'doorId', 'depotId', 'text', 'written', 'writtenBy', 'description', 'teledest')

# Format (Work in Progress)
"""
    <uint8>floor_level
    floorLevel < 60
        <loop>32x32

        <uint16>itemId
        <uint8>attributeCount / other
        
        itemId >= 100:
            every attributeCount (
                See attribute format
            )

        itemId == 50:
            <int32> Tile flags
            
        itemId == 51:
            <uint32> houseId
            
        itemId == 0:
            skip attributeCount fields
            
        {
            ; -> go to next tile
            | -> skip the remaining y tiles
            ! -> skip the remaining x and y tiles
            , -> more items
        }
        
    floorLevel == 60:
        <uint16>center X
        <uint16>center Y
        <uint8>center Z
        <uint8> Radius from center creature might walk
        <uint8> count (
            <uint8> type (61 for Monster, 62 for NPC)
            <uint8> nameLength
            <string> Name
             
            <int8> X from center
            <int8> Y from center
                
            <uint16> spawntime in seconds
                       
            }
        )
    Attribute format:
    
    {
        <uint8>attributeId
        <char>attributeType
        {
            attributeType == i (
                <int32>value
            )
            attributeType == s (
                <uint16>valueLength
                <string with length valueLength>value
            )
            attributeType == b (
                <bool>value
            )
            attributeType == l (
                <uint8>listItems
                <repeat this block for listItems times> -> value
            )
        }
        
        
    }
"""

def loadSectorMap(code, instanceId, baseX, baseY):
    thisSectorMap = [None, None, None, None,None, None, None, None,None, None, None, None,None, None, None, None]
    pos = 0
    codeLength = len(code)
    skip = False
    skip_remaining = False
    houseId = 0
    housePosition = None
    yRowGotItem = False
    
    # Avoid 1k calls to making the format :)
    # Pypy need a special treatment to avoid this.
    
    if sys.subversion[0] == 'PyPy':
        ll_unpack = struct.unpack
        l_unpack = lambda data: ll_unpack("<HB", data)
        long_unpack = lambda data: ll_unpack("<i", data)
        spawn_unpack = lambda data: ll_unpack("<HHBBB", data)
        creature_unpack  = lambda data: ll_unpack("<bbH", data)
    else:
        l_unpack = struct.Struct("<HB").unpack
        long_unpack = struct.Struct("<i").unpack
        creature_unpack = struct.Struct("<bbH").unpack
        spawn_unpack = struct.Struct("<HHBBB").unpack
    
    # Bind them locally, this is suppose to make a small speedup as well, local things can be more optimized :)
    # Pypy gain nothing, but CPython does.
    l_Item = game.item.Item
    l_Tile = Tile
    l_HouseTile = HouseTile
    
    # Also attempt to local the itemCache, pypy doesn't like this tho.
    l_itemCache = dummyItems
    l_attributes = attributeIds
    
    # Spawn commands
    l_getNPC = game.npc.getNPC
    l_getMonster = game.monster.getMonster
    
    # This is the Z loop (floor), we read the first byte
    while True:
        if pos >= codeLength:
           return thisSectorMap
           
        # First byte where we're at.
        level = ord(code[pos])
        pos += 1
        
        if level == 60:
            centerX, centerY, centerZ, centerRadius, creatureCount = spawn_unpack(code[pos:pos+7])
            
            pos += 7
                            
            # Mark a position
            centerPoint = Position(centerX, centerY, centerZ, instanceId)
                            
            # Here we use attrNr as a count for 
            for numCreature in xrange(creatureCount):
                creatureType = ord(code[pos])
                nameLength = ord(code[pos+1])
                name = code[pos+2:pos+nameLength+2]
                pos += 2 + nameLength
                spawnX, spawnY, spawnTime = creature_unpack(code[pos:pos+4])
                pos += 4
                if creatureType == 61:
                    creature = l_getMonster(name)
                else:
                    creature = l_getNPC(name)
                if creature:
                    creature.spawn(Position(centerX+spawnX, centerY+spawnY, centerZ, instanceId), radius=centerRadius, spawnTime=spawnTime, radiusTo=centerPoint)
                else:
                    print "Spawning of %s '%s' failed, it doesn't exist!" % ("Monster" if creatureType == 61 else "NPC", name)
                                    
            continue
        
        # An x level list for this floor
        xlevel = []
        
        # Speedup call.
        l_xlevel_append = xlevel.append
        
        # Loop over the 32 x rows
        for xr in xrange(32):
            # The real X position
            xPosition = xr + baseX
            
            # An y level list
            ywork = []
            
            # Speed up call
            l_ywork_append = ywork.append
            
            # Since we need to deal with skips we need to deal with counts and not a static loop (pypy will have a problem unroll this hehe)
            yr = 0
            
            while yr < 32:
                # The real Y position
                yPosition = yr + baseY
                
                # The items array and the flags for the Tile.
                items = []
                flags = 0
                
                # Speed up call
                l_items_append = items.append
                
                # We have no limit on the amount of items that a Tile might have. Loop until we hit a end.
                while True:
                    # uint16 itemId / type
                    # uint16 attrNr / count
                    itemId, attrNr = l_unpack(code[pos:pos+3])

                    # Do we have a positive id? If not its a blank tile
                    if itemId:
                        # Tile flags
                        if itemId == 50:
                            pos += 2
                            # int32
                            flags = long_unpack(code[pos:pos+4])[0]
                            pos += 5
                        
                        # HouseId?
                        elif itemId == 51:
                            pos += 2
                            # int32
                            houseId = long_unpack(code[pos:pos+4])[0]
                            housePosition = (xPosition, yPosition, level)
                            pos += 5
                            
                        elif attrNr:
                            pos += 3
                            attr = {}
                            for n in xrange(attrNr):
                                name = l_attributes[ord(code[pos])]
                                    
                                opCode = code[pos+1]
                                pos += 2
                                
                                if opCode == "i":
                                    pos += 4
                                    value = long_unpack(code[pos-4:pos])[0]
                                elif opCode == "s":
                                    valueLength = long_unpack(code[pos:pos+4])[0]
                                    pos += valueLength + 4
                                    value = code[pos-valueLength:pos]
                                elif opCode == "b":
                                    pos += 1
                                    value = bool(ord(code[pos-1]))
                                elif opCode == "l":
                                    value = []
                                    length = ord(code[pos])

                                    pos += 1
                                    for i in xrange(length):
                                        opCode = code[pos]
                                        pos += 1
                                        if opCode == "i":
                                            pos += 4
                                            item = long_unpack(code[pos-4:pos])[0]
                                        elif opCode == "s":
                                            valueLength = long_unpack(code[pos:pos+4])[0]
                                            pos += valueLength + 4
                                            item = code[pos-valueLength:pos]
                                        elif opCode == "b":
                                            pos += 1
                                            item = bool(ord(code[pos-1]))
                                        value.append(item)
                                        
                                attr[name] = value
                                
                            pos += 1
                            item = l_Item(itemId, **attr)
                            item.fromMap = True
                            l_items_append(item)
                        else:
                            pos += 4
                            try:
                                l_items_append(l_itemCache[itemId])
                            except KeyError:
                                item = l_Item(itemId)
                                item.tileStacked = True
                                item.fromMap = True
                                l_itemCache[itemId] = item
                                l_items_append(item)

                    else:
                        pos += 4
                        if attrNr:
                            for x in xrange(attrNr):
                                l_ywork_append(None)
                            yr += attrNr -1
                        else:
                            l_ywork_append(None)
                        yRowGotItem = True
                        
                    
                        
                    v = code[pos-1]
                    if v == ';': break
                    elif v == '|':
                        skip = True
                        break
                    elif v == '!':
                        skip = True
                        skip_remaining = True
                        break
                    # otherwise it should be ",", we don't need to vertify this.
                if items:
                    # For the PvP configuration option, yet allow scriptability. Add/Remove the flag.
                    if config.globalProtectionZone and not flags & TILEFLAGS_PROTECTIONZONE:
                        flags += TILEFLAGS_PROTECTIONZONE
                    elif not config.protectedZones and flags & TILEFLAGS_PROTECTIONZONE:
                        flags -= TILEFLAGS_PROTECTIONZONE
                    if houseId:
                        # Fix flags if necessary, TODO: Move this to map maker!
                        if config.protectedZones and not flags & TILEFLAGS_PROTECTIONZONE:
                            flags += TILEFLAGS_PROTECTIONZONE
                            
                        tile = l_HouseTile(items, flags)
                        tile.houseId = houseId
                        tile.position = housePosition
                        
                        
                        # Find and cache doors
                        for i in tile.getItems():
                            if i.hasAction("houseDoor"):
                                try:
                                    houseDoors[houseId].append(housePosition)
                                    break
                                except:
                                    houseDoors[houseId] = [housePosition]
                                
                        
                        if houseId in houseTiles:
                            houseTiles[houseId].append(tile)
                        else:
                            houseTiles[houseId] = [tile]
                            
                        try:
                            for item in game.house.houseData[houseId].data["items"][housePosition]:
                                tile.placeItem(item)
                        except KeyError:
                            pass
    
                        houseId = 0
                        housePosition = None
                        l_ywork_append(tile)
                    else:
                        l_ywork_append(l_Tile(items, flags))
                elif not yRowGotItem:
                    l_ywork_append(None)
                    yRowGotItem = False
                yr += 1

                if skip:
                    skip = False
                    break                
            l_xlevel_append(ywork)
            if skip_remaining:
                skip_remaining = False
                break
                
        thisSectorMap[level] = xlevel
           
### End New Map Format ###
def load(sectorX, sectorY, instanceId):
    sectorSum = (sectorX << 15) + sectorY
    
    if sectorSum in knownMap[instanceId]:
        return False
          
    print "Loading %d.%d.sec" % (sectorX, sectorY)
    t = time.time()
    
    # Attempt to load a sector file
    try:
        with io.open("data/map/%s%d.%d.sec" % (instances[instanceId], sectorX, sectorY), "rb") as f:
            knownMap[instanceId][sectorSum] = loadSectorMap(f.read(), instanceId, sectorX << 5, sectorY << 5)
    except IOError:
        # No? Mark it as empty
        knownMap[instanceId][sectorSum] = None
        return False
        
    print "Loading of %d.%d.sec took: %f" % (sectorX, sectorY, time.time() - t)    
    
    if config.performSectorUnload:
        reactor.callLater(config.performSectorUnloadEvery, _unloadMap, sectorX, sectorY, instanceId)
    
    scriptsystem.get('postLoadSector').runSync("%d.%d" % (sectorX, sectorY), None, None, sector=knownMap[instanceId][sectorSum], instanceId=instanceId)
    
    gc.collect()
    return True

# Map cleaner
def _unloadCheck(sectorX, sectorY, instanceId):
    # Calculate the x->x and y->y ranges
    # We're using a little higher values here to avoid reloading again 
    
    xMin = (sectorX * mapInfo.sectorSize[0]) + 14
    xMax = (xMin + mapInfo.sectorSize[0]) + 14
    yMin = (sectorY * mapInfo.sectorSize[1]) + 11
    yMax = (yMin + mapInfo.sectorSize[1]) + 11
    try:
        for player in game.player.allPlayers.viewvalues():
            pos = player.position # Pre get this one for sake of speed, saves us a total of 4 operations per player
            
            # Two cases have to match, the player got to be within the field, or be able to see either end (x or y)
            if instanceId == pos.instanceId and (pos[0] < xMax or pos[0] > xMin) and (pos[1] < yMax or pos[1] > yMin):
                return False # He can see us, cancel the unloading
    except:
        return False # Players was changed.
        
    return True
    
def _unloadMap(sectorX, sectorY, instanceId):
    print "Checking %d.%d.sec (instanceId %s)" % (sectorX, sectorY, instanceId)
    t = time.time()
    if _unloadCheck(sectorX, sectorY, instanceId):
        print "Unloading...."
        unload(sectorX, sectorY, instanceId)
        print "Unloading took: %f" % (time.time() - t)   
    reactor.callLater(config.performSectorUnloadEvery, _unloadMap, sectorX, sectorY, instanceId)
    
def unload(sectorX, sectorY, instanceId):
    sectorSum = (sectorX << 15) + sectorY
    try:
        del knownMap[instanceId][sectorSum]
    except:
        pass
