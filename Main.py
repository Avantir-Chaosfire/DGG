import random, os

from CardSet import *
from Game import *

#TODO
#gui?
#executable
#variablize magic numbers and strings

editionCountNames = ['first', 'second']

def main():
    rawCardSetsList = [CardSet(fileName) for fileName in os.listdir('sets') if not fileName.startswith('.') and os.path.isfile(os.path.join('sets', fileName))]

    cardSetEditionNames = {}
    cardSets = {}
    for cardSet in rawCardSetsList:
        cardSetNameInput = cardSet.name.lower()
        cardSets[cardSetNameInput] = cardSet
        cardSetEditionNames[cardSetNameInput] = (cardSetNameInput, cardSet.editionCount if cardSet.editionCount > 0 else 0)
        cardSetEditionNames[cardSetNameInput + ' all editions'] = (cardSetNameInput, 0)
        for editionIndex in range(cardSet.editionCount):
            cardSetEditionNames[cardSetNameInput + ' ' + editionCountNames[editionIndex] + ' edition'] = (cardSetNameInput, editionIndex + 1)

    print('Dominion Game Generator')
    print('')

    while True:
        setsToUse = {}

        print('Enter expansion names you want to use')

        while True:
            command = input().lower()

            args = command.split(' ')
            weight = 1

            try:
                weight = int(args[-1])
                args = args[:-1]
            except ValueError:
                pass

            command = ' '.join(args)
            
            if command == 'done':
                break
            elif command in cardSetEditionNames:
                if command in setsToUse:
                    print('Duplicate expansion')
                    continue
                else:
                    (cardSetName, edition) = cardSetEditionNames[command]
                    setsToUse[cardSetName] = (edition, weight)
            else:
                print('Unknown expansion')
                continue

        randomizerDeck = []
        kingdomPileCount = 0

        for (cardSetName, (edition, weight)) in setsToUse.items():
            pieces = cardSets[cardSetName].getPieces('kingdomPiles', edition)
            kingdomPileCount += len(pieces)
            for pieceType in ['events', 'landmarks', 'projects']:
                pieces += cardSets[cardSetName].getPieces(pieceType, edition)
            for piece in pieces:
                piece.weight = weight if piece.weight == None else piece.weight
                for i in range(weight):
                    randomizerDeck.append((piece, i))

        if kingdomPileCount < 10:
            print('Not enough kingdom cards to play with')
            print('')
            continue

        game = Game(cardSets)

        recommendedCount = 0

        while len(game.pieces['kingdomPiles']) < 10:
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
