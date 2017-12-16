from Card import *
from Set import *

class Promo(Set):
    def __init__(self):
        Set.__init__(self)

        promoFile = open('sets/Promo.cli', 'r')
        self.promoCards = [l[:-1] for l in promoFile.readlines()]
        promoFile.close()

        #Kingdom Cards
        self.addCard(Card('Black Market', 'kingdom', 'Promotional', 3))
        self.addCard(Card('Dismantle', 'kingdom', 'Promotional', 4))
        self.addCard(Card('Envoy', 'kingdom', 'Promotional', 4))
        self.addCard(Card('Governor', 'kingdom', 'Promotional', 5))
        self.addCard(Card('Prince', 'kingdom', 'Promotional', 8))

        self.addCard(Card('Sauna/Avanto', 'kingdom', 'Promotional', 4))
        self.addCard(Card('Stash', 'kingdom', 'Promotional', 5))
        self.addCard(Card('Walled Village', 'kingdom', 'Promotional', 4))

        #Events
        self.events.append(Card('Summon', 'event', 'Promotional', 5))

    def addCard(self, card):
        if card.name in self.promoCards:
            self.kingdomCards.append(card)

    def getExtraSupplyCards(self, kingdomCards, eventCards, landmarkCards):
        extraSupplyCards = []
        
        for kingdomCard in kingdomCards:
            if kingdomCard.name == 'Black Market':
                extraSupplyCards.append(Card('Black Market Deck', 'decks', 'Promotional'))

        return extraSupplyCards
