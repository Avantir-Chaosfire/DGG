import os, json, random

from Constants import *
from Piece import *

class CardSet:
    def __init__(self, fileName):
        self.pieces = {}

        with open(os.path.join(Constants.SETS_DIRECTORY_NAME, fileName)) as jsonFile:
            data = json.load(jsonFile)

        self.name = data.get(Constants.SET_NAME_ATTRIBUTE, fileName[:-len(Constants.CONFIG_FILE_EXTENSION)])
        self.addPieces(data.get(Constants.COMMON_ATTRIBUTE, {}), Constants.ALL_EDITIONS)

        self.editionCount = len(data.get(Constants.EDITIONS_ATTRIBUTE, []))
        for editionIndex in range(self.editionCount):
            self.addPieces(data[Constants.EDITIONS_ATTRIBUTE][editionIndex], editionIndex + 1)

    def addPieces(self, data, edition):
        for pieceType in Constants.PIECE_TYPES:
            for (name, properties) in data.get(pieceType, {}).items():
                if not pieceType in self.pieces:
                    self.pieces[pieceType] = []
                self.pieces[pieceType].append(Piece(name, self.name, edition, pieceType, properties))

    def getPieces(self, pieceType, edition):
        pieces = []

        for piece in self.pieces.get(pieceType, []):
            if piece.available and (piece.edition in [Constants.ALL_EDITIONS, edition] or edition == Constants.ALL_EDITIONS):
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
        if random.randint(0, Constants.KINGDOM_CARD_PILES - 1) < kingdomPilesFromCardSetCount:
            for pieceType in self.pieces.keys():
                for piece in self.pieces[pieceType]:
                    if piece.random:
                        result.append(piece)
        return result
