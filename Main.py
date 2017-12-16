from random import *
from importlib.util import *
from inspect import *

from SetDescription import *
from Card import *
from Set import *

#TODO
#gui?
#executable

def printCard(card, usingPotions, usingDebt, prefix = '', suffix = ''):
    message = prefix + '\t'
    if card.cost > -1:
        message += str(card.cost)
        if usingPotions and usingDebt:
            if card.potions == 0 and card.debt == 0:
                message += '        - '
            elif card.debt == 0:
                message += '(' + str(card.potions) + 'p)    - '
            elif card.potions == 0:
                message += '   (' + str(card.debt) + 'd) - '
            else:
                message += '(' + str(card.potions) + 'p,' + str(card.debt) + 'd) - '
        elif usingPotions:
            if card.potions == 0:
                message += '     - '
            else:
                message += '(' + str(card.potions) + 'p) - '
        elif usingDebt:
            if card.debt == 0:
                message += '     - '
            else:
                message += '(' + str(card.debt) + 'd) - '
        else:
            message += ' - '
    message += card.name + ' (' + card.setName + ')' + suffix
    print(message)

def stripTrailingNewline(line):
    if line[-1] == '\n':
        return line[:-1]
    else:
        return line

def main():
    setDescriptions = []

    setsFile = open('sets.sf', 'r')
    rawSets = setsFile.readlines()
    setsFile.close()

    for rawSet in rawSets:
        rawSet = stripTrailingNewline(rawSet)
        rawSetList = rawSet.split(':')
        if len(rawSetList) == 1:
            setDescriptions.append(SetDescription(rawSetList[0]))
        elif len(rawSetList) == 2:
            setDescriptions.append(SetDescription(rawSetList[0], rawSetList[1]))
        elif len(rawSetList) == 3:
            setDescriptions.append(SetDescription(rawSetList[0], rawSetList[1]))
            setDescriptions[-1].setArg(rawSetList[2])
        else:
            raise SyntaxError('Cannot read sets.sf')

    deck = {}

    for cardSetDescription in setDescriptions:
        spec = spec_from_file_location(cardSetDescription.fileName, 'sets/' + cardSetDescription.fileName + '.py')
        module = module_from_spec(spec)
        spec.loader.exec_module(module)
        for name, obj in getmembers(module):
            if isclass(obj) and issubclass(obj, Set) and not name == 'Set':
                if cardSetDescription.hasArg:
                    deck[cardSetDescription.setName.lower()] = obj(int(cardSetDescription.arg))
                else:
                    deck[cardSetDescription.setName.lower()] = obj()
                    
    print('Dominion Game Generator')
    print('')

    while True:
        setsToUse = []

        print('Enter expansion names you want to use')

        while True:
            setToUse = input().lower()
            
            if setToUse == 'done':
                break
            elif setToUse in deck.keys():
                setsToUse.append(setToUse)
            else:
                print('Unknown expansion')

        randomizerDeck = []
        possibleKingdomCards = []

        for cardSet in setsToUse:
            possibleKingdomCards += deck[cardSet].getKingdomCards()
            randomizerDeck += deck[cardSet].getKingdomCards()
            randomizerDeck += deck[cardSet].getEvents()
            randomizerDeck += deck[cardSet].getLandmarks()

        if len(possibleKingdomCards) < 10:
            print('Not enough kingdom cards to play with')
            print('')
            continue

        usingDebt = False
        eventsUsingDebt = False
        usingPotions = False
        eventsUsingPotions = False
        hasEvents = False
        hasLandmarks = False

        kingdomCards = []
        eventCards = []
        landmarkCards = []
        extraSupplyCards = []

        recommendedEvents = 0
        recommendedLandmarks = 0

        i = 0
        while i < 10:
            usingCardIndex = randint(0, len(randomizerDeck) - 1)

            usingCard = randomizerDeck[usingCardIndex]
            
            duplicate = False
            for card in kingdomCards + eventCards + landmarkCards:
                if usingCard.name == card.name:
                    duplicate = True

            if not duplicate:
                del randomizerDeck[usingCardIndex]

                if usingCard.kind == 'kingdom' and usingCard.potions > 0:
                    usingPotions = True

                if usingCard.kind == 'event' and usingCard.potions > 0:
                    eventsUsingPotions = True
                    
                if usingCard.kind == 'kingdom' and usingCard.debt > 0:
                    usingDebt = True

                if usingCard.kind == 'event' and usingCard.debt > 0:
                    eventsUsingDebt = True

                if usingCard.kind == 'kingdom':
                    kingdomCards.append(usingCard)
                    i += 1
                elif usingCard.kind == 'event':
                    eventCards.append(usingCard)
                    if recommendedEvents + recommendedLandmarks < 2:
                        recommendedEvents += 1
                    hasEvents = True
                elif usingCard.kind == 'landmark':
                    landmarkCards.append(usingCard)
                    if recommendedEvents + recommendedLandmarks < 2:
                        recommendedLandmarks += 1
                    hasLandmarks = True

        for cardSet in setsToUse:
            extraSupplyCards += deck[cardSet].getExtraSupplyCards(kingdomCards, eventCards, landmarkCards)

        resolvedExtraSupplyCards = []

        i = 0
        while i < len(extraSupplyCards):
            j = i + 1
            while j < len(extraSupplyCards):
                if extraSupplyCards[i].name == extraSupplyCards[j].name:
                    extraSupplyCards[i].setName += '/' + extraSupplyCards[j].setName
                    resolvedExtraSupplyCards.append(j)
                j += 1
            i += 1

        i = len(resolvedExtraSupplyCards) - 1
        while i > -1:
            index = resolvedExtraSupplyCards[i]
            del extraSupplyCards[index]
            i -= 1

        print('')
        print('Kingdom Cards')
        for i in range(0, 20):
            for j in range(0, 5):
                for k in range(0, 20):
                    for kingdomCard in kingdomCards:
                        if kingdomCard.cost == i and kingdomCard.potions == j and kingdomCard.debt == k:
                            printCard(kingdomCard, usingPotions, usingDebt)
        print('')

        if len(extraSupplyCards) > 0:
            print('Extra Materials')
            kinds = []
            for extraSupplyCard in extraSupplyCards:
                if extraSupplyCard.kind not in kinds:
                    kinds.append(extraSupplyCard.kind)
            for kind in kinds:
                print('\t' + kind.title())
                for extraSupplyCard in extraSupplyCards:
                    if extraSupplyCard.kind == kind:
                        printCard(extraSupplyCard, False, False, '\t')
            print('')
        
        if hasEvents:
            print('Events')
            for i in range(0, 20):
                for j in range(0, 5):
                    for k in range(0, 20):
                        l = 0
                        for eventCard in eventCards:
                            if eventCard.cost == i and eventCard.potions == j and eventCard.debt == k:
                                if l < recommendedEvents:
                                    printCard(eventCard, eventsUsingPotions, eventsUsingDebt, '', ' (Recommended)')
                                else:
                                    printCard(eventCard, eventsUsingPotions, eventsUsingDebt)
                            l += 1
            print('')

        if hasLandmarks:
            print('Landmarks')
            i = 0
            for landmarkCard in landmarkCards:
                if i < recommendedLandmarks:
                    printCard(landmarkCard, False, False, '', ' (Recommended)')
                else:
                    printCard(landmarkCard, False, False)
                i += 1
            print('')

if __name__ == '__main__':
    main()
