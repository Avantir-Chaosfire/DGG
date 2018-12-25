import random

from Constants import *
from FormatProperties import *

class Game:
    def __init__(self, cardSets):
        self.pieces = {}
        self.pieces[Constants.KINGDOM_PILES_ATTRIBUTE] = []
        self.formatProperties = FormatProperties()
        self.cardSets = cardSets

        self.recommendedCount = 0

    def add(self, piece):
        if not self.contains(piece):
            self.formatProperties.add(piece)

            if piece.kind not in self.pieces:
                self.pieces[piece.kind] = []
            self.pieces[piece.kind].append(piece)

            if piece.kind in [Constants.EVENTS_ATTRIBUTE, Constants.LANDMARKS_ATTRIBUTE, Constants.PROJECTS_ATTRIBUTE] and self.recommendedCount < 2:
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
                kingdomPilesFromCardSetCount = len([piece for piece in self.pieces[Constants.KINGDOM_PILES_ATTRIBUTE] if piece.setName == cardSet.name])
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
                    uniquePieces[piece.name].setDisplayName += Constants.MULTIPLE_SET_NAME_SEPARATOR + piece.setDisplayName
                else:
                    uniquePieces[piece.name] = piece
            self.pieces[pieceType] = uniquePieces.values()

        #Select piles
        for pieceType in self.pieces.keys():
            for piece in self.pieces[pieceType]:
                if piece.select:
                    list(self.pieces[Constants.KINGDOM_PILES_ATTRIBUTE])[random.randint(0, Constants.KINGDOM_CARD_PILES - 1)].selectedBy.append(piece.name)

    def print(self):
        for pieceType in Constants.PIECE_TYPES:
            if len(self.pieces.get(pieceType, [])) > 0:
                print('')
                print(Constants.PIECE_TYPE_DISPLAY_NAMES[pieceType])
                
                for piece in sorted(self.pieces[pieceType], key = lambda p: (p.cost, p.potions, p.debt)):
                    piece.print(self.formatProperties)
