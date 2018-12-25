import random

from FormatProperties import *

class Game:
    PIECE_TYPE_DISPLAY_NAMES = {
        'kingdomPiles': 'Kingdom Cards',
        'startingDeck': 'Starting Deck',
        'trash': 'Trash',
        'events': 'Events',
        'landmarks': 'Landmarks',
        'projects': 'Projects',
        'extraSupplyPiles': 'Supply',
        'nonSupplyPiles': 'Non-Supply',
        'extraMaterials': 'Materials'
    }
    
    def __init__(self, cardSets):
        self.pieces = {}
        self.pieces['kingdomPiles'] = []
        self.formatProperties = FormatProperties()
        self.cardSets = cardSets

        self.recommendedCount = 0

    def add(self, piece):
        if not self.contains(piece):
            self.formatProperties.add(piece)

            if piece.kind not in self.pieces:
                self.pieces[piece.kind] = []
            self.pieces[piece.kind].append(piece)

            if piece.kind in ['events', 'landmarks', 'projects'] and self.recommendedCount < 2:
                piece.recommended = True
                self.recommendedCount += 1

            for pieceName in piece.requires:
                requiredPiece = self.cardSets[piece.setName.lower()].getPiece(pieceName)
                if not requiredPiece == None:
                    self.add(requiredPiece)
                else:
                    print('WARNING: Cannot find "' + pieceName + '" in ' + piece.setName + '.')

    def contains(self, targetPiece):
        for pieceType in self.pieces.keys():
            for piece in self.pieces[pieceType]:
                if targetPiece.name == piece.name and targetPiece.setName == piece.setName:
                    return True
        return False

    def complete(self, setsToUse):
        #Select randoms
        piecesToAdd = []
        for cardSet in self.cardSets.values():
            cardSetKeyName = cardSet.name.lower()
            if cardSetKeyName in setsToUse:
                (edition, _) = setsToUse[cardSetKeyName]
                kingdomPilesFromCardSetCount = len([piece for piece in self.pieces['kingdomPiles'] if piece.setName == cardSet.name])
                if kingdomPilesFromCardSetCount > 0:
                    for pieceType in self.pieces.keys():
                        piecesToAdd += cardSet.getRandomPieces(pieceType, kingdomPilesFromCardSetCount, edition)
        for piece in piecesToAdd:
            self.add(piece)
        
        #Resolve Duplicates
        for pieceType in self.pieces.keys():
            uniquePieces = {}
            for piece in self.pieces[pieceType]:
                if piece.name in uniquePieces:
                    uniquePieces[piece.name].setName += '/' + piece.setName
                else:
                    uniquePieces[piece.name] = piece
            self.pieces[pieceType] = uniquePieces.values()

        #Select piles
        for pieceType in self.pieces.keys():
            for piece in self.pieces[pieceType]:
                if piece.select:
                    list(self.pieces['kingdomPiles'])[random.randint(0, 9)].selectedBy.append(piece.name)

    def print(self):
        for pieceType in ['kingdomPiles', 'events', 'landmarks', 'projects', 'startingDeck', 'extraSupplyPiles', 'nonSupplyPiles', 'trash', 'extraMaterials']:
            if len(self.pieces.get(pieceType, [])) > 0:
                print('')
                print(Game.PIECE_TYPE_DISPLAY_NAMES[pieceType])
                
                for piece in sorted(self.pieces[pieceType], key = lambda p: (p.cost, p.potions, p.debt)):
                    piece.print(self.formatProperties)
