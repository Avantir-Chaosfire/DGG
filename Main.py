import random, os, json

from Constants import *
from CardSet import *
from Game import *
from InputParser import *

#TODO
#gui?
#executable

def main():
    rawCardSetsList = [CardSet(fileName) for fileName in os.listdir(Constants.SETS_DIRECTORY_NAME) if not fileName.startswith('.') and os.path.isfile(os.path.join(Constants.SETS_DIRECTORY_NAME, fileName))]

    cardSetEditionNames = {}
    cardSets = {}
    for cardSet in rawCardSetsList:
        cardSetNameInput = cardSet.name.lower()
        cardSets[cardSetNameInput] = cardSet
        cardSetEditionNames[cardSetNameInput] = (cardSetNameInput, cardSet.editionCount if cardSet.editionCount > 0 else Constants.ALL_EDITIONS)
        cardSetEditionNames[cardSetNameInput + ' all editions'] = (cardSetNameInput, Constants.ALL_EDITIONS)
        for editionIndex in range(cardSet.editionCount):
            cardSetEditionNames[cardSetNameInput + ' ' + Constants.EDITION_COUNT_NAMES[editionIndex] + ' edition'] = (cardSetNameInput, editionIndex + 1)

    with open(Constants.CONFIGURATION_FILE_NAME) as configFile:
        data = json.load(configFile)

    macros = data.get('macros', {})

    print('Dominion Game Generator')
    print('')

    while True:
        print('Enter expansion names you want to use')
        
        inputParser = InputParser(macros, cardSetEditionNames)
        setsToUse = inputParser.getSetsToUse()
        
        randomizerDeck = []
        kingdomPileCount = 0

        for (cardSetName, (edition, weight)) in setsToUse.items():
            pieces = cardSets[cardSetName].getPieces(Constants.KINGDOM_PILES_ATTRIBUTE, edition)
            kingdomPileCount += len(pieces)
            for pieceType in [Constants.EVENTS_ATTRIBUTE, Constants.LANDMARKS_ATTRIBUTE, Constants.PROJECTS_ATTRIBUTE]:
                pieces += cardSets[cardSetName].getPieces(pieceType, edition)
            for piece in pieces:
                piece.weight = weight #if piece.weight == None else piece.weight
                for i in range(weight):
                    randomizerDeck.append((piece, i))

        if kingdomPileCount < Constants.KINGDOM_CARD_PILES:
            print('Not enough kingdom cards to play with')
            print('')
            continue

        game = Game(cardSets)

        while len(game.pieces[Constants.KINGDOM_PILES_ATTRIBUTE]) < Constants.KINGDOM_CARD_PILES:
            chosenPieceIndex = random.randint(0, len(randomizerDeck) - 1)

            (chosenPiece, weightIndex) = randomizerDeck[chosenPieceIndex]
            startOfchosenPieceRange = chosenPieceIndex - weightIndex
            endOfchosenPieceRange = chosenPieceIndex + (chosenPiece.weight - weightIndex)
            del randomizerDeck[startOfchosenPieceRange:endOfchosenPieceRange]

            game.add(chosenPiece)

        game.complete(setsToUse)
        game.print()
        print('')

if __name__ == '__main__':
    main()
