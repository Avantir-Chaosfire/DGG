from Card import *
from Set import *

class Seaside(Set):
    def __init__(self):
        Set.__init__(self)

        #Kingdom Cards
        self.kingdomCards.append(Card('Ambassador', 'kingdom', 'Seaside', 3))
        self.kingdomCards.append(Card('Bazaar', 'kingdom', 'Seaside', 5))
        self.kingdomCards.append(Card('Caravan', 'kingdom', 'Seaside', 4))
        self.kingdomCards.append(Card('Cutpurse', 'kingdom', 'Seaside', 4))
        self.kingdomCards.append(Card('Embargo', 'kingdom', 'Seaside', 2))

        self.kingdomCards.append(Card('Explorer', 'kingdom', 'Seaside', 5))
        self.kingdomCards.append(Card('Fishing Village', 'kingdom', 'Seaside', 3))
        self.kingdomCards.append(Card('Ghost Ship', 'kingdom', 'Seaside', 5))
        self.kingdomCards.append(Card('Haven', 'kingdom', 'Seaside', 2))
        self.kingdomCards.append(Card('Island', 'kingdom', 'Seaside', 4))

        self.kingdomCards.append(Card('Lighthouse', 'kingdom', 'Seaside', 2))
        self.kingdomCards.append(Card('Lookout', 'kingdom', 'Seaside', 3))
        self.kingdomCards.append(Card('Merchant Ship', 'kingdom', 'Seaside', 5))
        self.kingdomCards.append(Card('Native Village', 'kingdom', 'Seaside', 2))
        self.kingdomCards.append(Card('Navigator', 'kingdom', 'Seaside', 4))

        self.kingdomCards.append(Card('Outpost', 'kingdom', 'Seaside', 5))
        self.kingdomCards.append(Card('Pearl Diver', 'kingdom', 'Seaside', 2))
        self.kingdomCards.append(Card('Pirate Ship', 'kingdom', 'Seaside', 4))
        self.kingdomCards.append(Card('Salvager', 'kingdom', 'Seaside', 4))
        self.kingdomCards.append(Card('Sea Hag', 'kingdom', 'Seaside', 4))

        self.kingdomCards.append(Card('Smugglers', 'kingdom', 'Seaside', 3))
        self.kingdomCards.append(Card('Tactician', 'kingdom', 'Seaside', 5))
        self.kingdomCards.append(Card('Treasure Map', 'kingdom', 'Seaside', 4))
        self.kingdomCards.append(Card('Treasury', 'kingdom', 'Seaside', 5))
        self.kingdomCards.append(Card('Warehouse', 'kingdom', 'Seaside', 3))
        
        self.kingdomCards.append(Card('Wharf', 'kingdom', 'Seaside', 5))

    def getExtraSupplyCards(self, kingdomCards, eventCards, landmarkCards):
        extraSupplyCards = []
        
        for kingdomCard in kingdomCards:
            if kingdomCard.name == 'Embargo':
                extraSupplyCards.append(Card('Embargo Tokens', 'tokens', 'Seaside'))
            if kingdomCard.name == 'Island':
                extraSupplyCards.append(Card('Island Mat', 'mats', 'Seaside'))
            if kingdomCard.name == 'Native Village':
                extraSupplyCards.append(Card('Native Village Mat', 'mats', 'Seaside'))
            if kingdomCard.name == 'Pirate Ship':
                extraSupplyCards.append(Card('Pirate Ship Mat', 'mats', 'Seaside'))
                extraSupplyCards.append(Card('Coin Tokens', 'tokens', 'Seaside'))

        return extraSupplyCards
