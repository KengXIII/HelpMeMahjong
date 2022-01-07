from tile import Tile, HonorTile, SuitedTile

class Hand:
    def __init__(self, insideTiles):
        self.insideTiles = insideTiles
        self.outsideTiles = []
        self.categories = {
            "Circle": [],
            "Number": [],
            "Bamboo": [],
            "Honor": []
        }
        self.sortIntoCategories()
        # print("Initialized Tiles")
        # self.printInCategories()

    def printInCategories(self):
        for key, value in self.categories.items():
            print(key, end=": ")
            for tile in value:
                print(tile, end=" ")
            print("")
        print("")

    def printOutsideTiles(self):
        print("Outside Tiles: ", end="")
        for i in range(len(self.outsideTiles)):
            print(self.outsideTiles[i], end=" ")
        print("")
        print("")

    def printAll(self):
        print("Hand: ", end="")
        for tile in self.insideTiles:
            print(tile, end=" ")
        print("")
        print("")

    def sort(self):
        self.insideTiles = sorted(self.insideTiles, key=lambda tile: (tile.category, tile.number))
        self.outsideTiles = sorted(self.outsideTiles, key=lambda tile: (tile.category, tile.number))

    def sortIntoCategories(self):
        self.sort()
        self.categories = {
            "Circle": [],
            "Number": [],
            "Bamboo": [],
            "Honor": []
        }
        for tile in self.insideTiles:
            if tile.category == "Circle" or tile.category == "Bamboo" or tile.category == "Number":
                self.categories.get(tile.category).append(tile)
            else:
                self.categories['Honor'].append(tile)
        for tile in self.outsideTiles:
            if tile.category == "Circle" or tile.category == "Bamboo" or tile.category == "Number":
                self.categories.get(tile.category).append(tile)
            else:
                self.categories['Honor'].append(tile)

    def addTile(self, tile):
        self.insideTiles.append(tile)
        self.sort()
        self.sortIntoCategories()
        self.printAll()
        # print(f'Updated Tiles after adding {str(tile)}')
        # self.printInCategories()

    def removeTile(self, tile):
        for insideTile in self.insideTiles:
            if insideTile == tile and tile.category in Tile.suitedTiles:
                self.insideTiles.remove(insideTile)
                self.categories[insideTile.category].remove(insideTile)
                # print(f'Updated Tiles after removing {str(tile)}')
                # self.printInCategories()
            elif insideTile == tile:
                self.insideTiles.remove(insideTile)
                self.categories['Honor'].remove(insideTile)
                return

    def replaceTile(self, removedTile, addedTile):
        self.removeTile(removedTile)
        self.addTile(addedTile)

    def Pong(self, removedTile, addedTile):

        found = False

        for i in range(len(self.insideTiles) - 2):
            if self.insideTiles[i] == self.insideTiles[i + 1] and self.insideTiles[i] == addedTile:
                self.outsideTiles.append(addedTile)
                self.outsideTiles.append(addedTile)
                self.outsideTiles.append(addedTile)
                self.removeTile(addedTile)
                self.removeTile(addedTile)
                self.removeTile(removedTile)
                self.printOutsideTiles()
                found = True
                break
            else:
                continue

        if not found:
            print("No Pong found.")

    def Chi(self, removedTile, consecTile1, consecTile2, addedTile):

        if SuitedTile.isConsecutiveThreeTile(consecTile1, consecTile2, addedTile):
            self.removeTile(consecTile1)
            self.removeTile(consecTile2)
            self.removeTile(removedTile)
            self.outsideTiles.append(consecTile1)
            self.outsideTiles.append(consecTile2)
            self.outsideTiles.append(addedTile)
            self.sort()
            self.printOutsideTiles()
        else:
            print("No consecutive tiles found.")

    # Gets all the possible set of 3 combinations in given tiles
    @classmethod
    def getAllPossibleSets(cls, tiles):

        sets = []
        # Add all possible pongs
        for i in range(len(tiles) - 2):
            if tiles[i] == tiles[i + 1] and tiles[i + 1] == tiles[i + 2]:
                sets.append([tiles[i], tiles[i + 1], tiles[i + 2]])
        # Add all possible chis
        for i in range(len(tiles)):
            for j in range(i + 1, len(tiles)):
                for k in range(j + 1, len(tiles)):
                    if SuitedTile.isConsecutiveThreeTile(tiles[i], tiles[j], tiles[k]):
                        sets.append([tiles[i], tiles[j], tiles[k]])
        return sets

    # Appends any possible combinations to allCombis
    @classmethod
    def getAllPossibleSetCombisHelper(cls, tiles, sets, allCombis):

        # for each possible set
        for set in sets:
            copyOfTiles = tiles.copy()
            hand = Hand(copyOfTiles)
            # removes all the tiles from current set
            for tile in set:
                hand.removeTile(tile)

            remainderSets = Hand.getAllPossibleSets(hand.insideTiles)

            if len(remainderSets) == 0:
                return

            newCombis = []
            for remainderSet in remainderSets:
                linkedSet = remainderSet + set
                newCombis.append(linkedSet)
                linkedSet = sorted(linkedSet, key=lambda tile: (tile.category, tile.number))
                if linkedSet not in allCombis:
                    allCombis.append(linkedSet)
                Hand.getAllPossibleSetCombisHelper(hand.insideTiles, newCombis, allCombis)

    @classmethod
    def getAllPossibleSetCombis(cls, tiles):
        newCombis = []
        Hand.getAllPossibleSetCombisHelper(tiles, Hand.getAllPossibleSets(tiles), newCombis)

        maxLenSoFar = 0
        for combi in newCombis:
            maxLenSoFar = max(maxLenSoFar, len(combi))

        finalCombis = []
        for combi in newCombis:
            if len(combi) == maxLenSoFar:
                finalCombis.append(combi)

        return finalCombis

    # Returns lone tiles from a list of tiles (tiles that can be thrown without affecting combos)
    @classmethod
    def getLoneTiles(cls, tiles):
        allCombis = Hand.getAllPossibleSetCombis(tiles)
        loneTileIdxs = set()

        for i in range(len(tiles)):
            for combi in allCombis:
                copyOfCombi = combi.copy()
                if tiles[i] not in copyOfCombi:
                    loneTileIdxs.add(i)
                else:
                    copyOfCombi.remove(tiles[i])

        loneTiles = []
        for i in list(loneTileIdxs):
            loneTiles.append(tiles[i])
        return loneTiles

    # Gets possible tiles to wait for
    @classmethod
    def getTilesToThrow(cls, tiles):
        loneTiles = Hand.getLoneTiles(tiles)
        filteredLoneTiles = []
        for i in range(len(loneTiles) - 1):
            if ((i == 0 and loneTiles[i] != loneTiles[i + 1])
                    or ((i == len(loneTiles) - 1) and loneTiles[i] != loneTiles[i - 1])
                    or (loneTiles[i] != loneTiles[i - 1] and loneTiles[i] != loneTiles[i + 1])):
                filteredLoneTiles.append(loneTiles[i])

        maxNumPotentialTiles = 0
        maxIdxs = []
        for i in range(len(filteredLoneTiles)):
            copyOfTiles = tiles.copy()
            copyOfTiles.remove(tiles[i])
            numPotentialTiles = len(Hand.getPotentialTiles(copyOfTiles))
            print(f'{filteredLoneTiles[i]}: {numPotentialTiles}')
            if numPotentialTiles > maxNumPotentialTiles:
                maxNumPotentialTiles = numPotentialTiles
                maxIdxs = [i]
            elif numPotentialTiles == maxNumPotentialTiles:
                maxIdxs.append(i)

        def findFurthestTile(tileList):
            maxDist = 0
            if len(tileList) == 0:
                return
            tileThrown = tileList[0]
            for idx in maxIdxs:
                dist = abs(tileList[idx].number - 5)
                if dist > maxDist:
                    maxDist = dist
                    tileThrown = tileList[idx]
            return tileThrown

        tileThrown = findFurthestTile(filteredLoneTiles)
        tileThrownFromLoneTileList = findFurthestTile(loneTiles)

        if len(filteredLoneTiles) != 0:
            print("Throwing from filtered list")
            return tileThrown
        elif len(loneTiles) != 0:
            print("Throwing from lone tile list")
            return tileThrownFromLoneTileList
        else:
            print("No tile found")
            return None

    # marks hand as being used in winning hand or not
    @classmethod
    def markHand(cls, set, isWinningHand):
        for tile in set:
            tile.isInsideWinningHand = isWinningHand

    def correctConfigOfWinningHand(self):
        # Winning hand should have 4 sets of 3 and 1 pair of 2

        if len(self.insideTiles + self.outsideTiles) != 14:
            return False
        else:
            sets = 0
            pairs = 0
            for key, value in self.categories.items():
                if len(value) % 3 == 2:
                    pairs += 1
                    sets += int(len(value) / 3)
                elif len(value) % 3 == 0:
                    sets += int(len(value) / 3)
                else:
                    return False
            if sets == (4 - len(self.outsideTiles) / 3) and pairs == 1:
                return True

    def isWinningHand(self):
        if self.correctConfigOfWinningHand():
            sum = 0
            count = 0
            Hand.markHand(self.insideTiles, False)
            for tile in self.insideTiles:
                sum += tile.number

            configs = [[0, 3, 6, 9], [2, 5, 8], [1, 4, 7]]
            moduloResult = sum % 3
            pairIndexes = []
            # Checks if tile satisfies the modulo condition and has a duplicate
            for i in range(len(self.insideTiles) - 1):
                if self.insideTiles[i].number in configs[moduloResult] and self.insideTiles[i] == self.insideTiles[i + 1]:
                    pairIndexes.append([i, i + 1])

            for pair in pairIndexes:
                # Creates a copy of tiles without specific pair of duplicates
                copyOfTiles = self.insideTiles.copy()

                copyOfTiles[pair[1]].isInsideWinningHand = True
                copyOfTiles[pair[0]].isInsideWinningHand = True
                count += 2

                # looks for pongs (3 of a kind)
                for i in range(len(copyOfTiles) - 2):
                    areTheSame = copyOfTiles[i] == copyOfTiles[i + 1] and copyOfTiles[i + 1] == copyOfTiles[i + 2]
                    areAllNotInsideWinningHand = not (copyOfTiles[i].isInsideWinningHand
                                                      or copyOfTiles[i + 1].isInsideWinningHand
                                                      or copyOfTiles[i + 2].isInsideWinningHand)
                    # print(f'{copyOfTiles[i]}, {copyOfTiles[i + 1]}, {copyOfTiles[i + 2]} are {areTheSame}')
                    if areTheSame and areAllNotInsideWinningHand:
                        copyOfTiles[i + 2].isInsideWinningHand = True
                        copyOfTiles[i + 1].isInsideWinningHand = True
                        copyOfTiles[i].isInsideWinningHand = True
                        count += 3

                # looks for set of 3 consecutive tiles
                for i in range(len(copyOfTiles)):
                    if not isinstance(copyOfTiles[i], SuitedTile) or copyOfTiles[i].isInsideWinningHand:
                        continue
                    else:
                        for j in range(i + 1, len(copyOfTiles)):
                            if not isinstance(copyOfTiles[j], SuitedTile) or copyOfTiles[j].isInsideWinningHand:
                                continue
                            else:
                                for k in range(j + 1, len(copyOfTiles)):
                                    if copyOfTiles[k].isInsideWinningHand:
                                        continue
                                    elif (SuitedTile.isConsecutiveThreeTile(copyOfTiles[i],
                                                                                  copyOfTiles[j],
                                                                                  copyOfTiles[k])):
                                        copyOfTiles[i].isInsideWinningHand = True
                                        copyOfTiles[j].isInsideWinningHand = True
                                        copyOfTiles[k].isInsideWinningHand = True
                                        count +=3
                                        break
                
                
                if count == len(copyOfTiles):
                    return True
                
                Hand.markHand(self.insideTiles, False)
            return False
        else:
            # print("Incorrect configuration")
            return False

    # Returns list of tiles to throw
    @classmethod
    def getPotentialTiles(cls, tiles):
        potentialConsecutives = []
        loneTiles = Hand.getLoneTiles(tiles)

        for tile in loneTiles:
            copyOfTiles = tiles.copy()
            copyOfTiles.remove(tile)

        for tile1 in loneTiles:
            for tile2 in copyOfTiles:
                potential = SuitedTile.findConsecutiveTile(tile1, tile2)
                for tile in potential:
                    if tile not in potentialConsecutives:
                        potentialConsecutives.append(tile)

                tile = Tile.findSimilarTile(tile1, tile2)
                if tile is not None and tile not in potentialConsecutives:
                    potentialConsecutives.append(tile)

        return potentialConsecutives

    def isOneTileFromWinning(self):
        allTiles = []
        winningTiles = []

        if (len(self.insideTiles) + len(self.outsideTiles)) != 13:
            return []

        for cat in Tile.suitedTiles:
            for i in range(1, 10):
                tile = SuitedTile(category=cat, number=i)
                allTiles.append(tile)

        for cat in Tile.honorTiles:
            tile = HonorTile(category=cat)
            allTiles.append(tile)

        for tile in allTiles:
            copyOfTiles = self.insideTiles.copy()
            Hand.markHand(copyOfTiles, False)
            copyOfTiles.append(tile)
            copyOfTiles = sorted(copyOfTiles, key=lambda x: (x.category, x.number))
            hand = Hand(copyOfTiles)
            if hand.isWinningHand():
                winningTiles.append(tile)

        if len(winningTiles) == 0:
            print("No winning tiles available")
            return []
        else:
            return winningTiles
