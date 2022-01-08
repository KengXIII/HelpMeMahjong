class Tile:

    def __init__(self, category, number):
        self.category = category
        self.number = number
        self.isInsideWinningHand = False

    suitedTiles = ["Circle", "Bamboo", "Number"]
    honorTiles = ["NorthWind",  "EastWind", "SouthWind", "WestWind", "RedDragon", "WhiteDragon", "GreenDragon"]

    @classmethod
    def isSameThreeTiles(cls, tile1, tile2, tile3):
        return tile1 == tile2 and tile2 == tile3

    @classmethod
    def findSimilarTile(cls, tile1, tile2):
        if tile1 != tile2:
            return None
        else:
            return tile1

    def __eq__(self, other):
        return self.category == other.category and self.number == other.number

    def __str__(self):
        return str(self.number) + self.category

    def __hash__(self):
        return hash((self.category, self.number))

    def setIsInsideWinningHand(self, val):
        self.isInsideWinningHand = val


class SuitedTile(Tile):

    def __init__(self, category, number):
        self.category = category
        self.number = number
        self.isInsideWinningHand = False

    def __str__(self):
        return str(self.number) + self.category

    def __eq__(self, other):
        return self.category == other.category and self.number == other.number
    
    def __hash__(self):
        return hash((self.category, self.number))

    def __lt__(self, other):
        return self.number < other.number

    # Assumes sorted list
    @classmethod
    def isConsecutiveThreeTile(cls, tile1, tile2, tile3):
        if tile1.category == tile2.category and tile2.category == tile3.category:
            tiles = [tile1, tile2, tile3]
            tiles.sort()
            if tiles[2].number - tiles[1].number == 1 and tiles[1].number - tiles[0].number == 1:
                return True
        else:
            return False

    # Finds list of tile(s) required to form a consecutive set, returns None if cannot be found
    @classmethod
    def findConsecutiveTile(cls, tile1, tile2):
        if tile1.category != tile2.category:
            return []

        if tile1.number > tile2.number:
            biggerNumber = tile1.number
            smallerNumber = tile2.number
        else:
            biggerNumber = tile2.number
            smallerNumber = tile1.number

        category = tile1.category

        if biggerNumber - smallerNumber == 1:
            if biggerNumber != 9 and smallerNumber != 1:
                return [SuitedTile(category, biggerNumber + 1),
                        SuitedTile(category, smallerNumber - 1)]
            elif biggerNumber == 9:
                return [SuitedTile(category, smallerNumber - 1)]
            else:
                return [SuitedTile(category, biggerNumber + 1)]
        elif biggerNumber - smallerNumber == 2:
            return [SuitedTile(category, biggerNumber - 1)]
        else:
            return []

    def setIsInsideWinningHand(self, val):
        self.isInsideWinningHand = val

class HonorTile(Tile):
    def __init__(self, category):
        self.category = category
        self.number = 0
        self.isInsideWinningHand = False

    def __str__(self):
        return self.category

    def __eq__(self, other):
        return self.category == other.category
    
    def __hash__(self):
        return hash((self.category, self.number))
    
    def setIsInsideWinningHand(self, val):
        self.isInsideWinningHand = val
