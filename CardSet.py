import os, json, random

from Piece import *

class CardSet:
    PIECE_TYPES = [
        'kingdomPiles',
        'startingDeck',
        'trash',
        'events',
        'landmarks',
        'projects',
        'extraSupplyPiles',
        'nonSupplyPiles',
        'extraMaterials'
    ]
    
    def __init__(self, fileName):
        self.pieces = {}

        with open(os.path.join('sets', fileName)) as jsonFile:
            data = json.load(jsonFile)

        self.name = data.get('name', fileName[:-len('.json')])
        self.addPieces(data.get('common', {}), 0)

        self.editionCount = len(data.get('editions', []))
        for editionIndex in range(self.editionCount):
            self.addPieces(data['editions'][editionIndex], editionIndex + 1)

    def addPieces(self, data, edition):
        for pieceType in CardSet.PIECE_TYPES:
            for (name, properties) in data.get(pieceType, {}).items():
                if not pieceType in self.pieces:
                    self.pieces[pieceType] = []
                self.pieces[pieceType].append(Piece(name, self.name, edition, pieceType, properties))

    def getPieces(self, pieceType, edition):
        pieces = []

        for piece in self.pieces.get(pieceType, []):
            if piece.available and (piece.edition in [0, edition] or edition == 0):
                pieces.append(piece)
        return pieces

    def getPiece(self, pieceName):
        for pieceType in self.pieces.keys():
            for piece in self.pieces[pieceType]:
                if piece.name == pieceName:
                    return piece
        return None

    def getRandomPieces(self, pieceType, kingdomPilesFromCardSetCount, edition):
        result = []
        for pieceType in self.pieces.keys():
            for piece in self.pieces[pieceType]:
                if piece.random and random.randint(0, 9) < kingdomPilesFromCardSetCount:
                    result.append(piece)
        return result
