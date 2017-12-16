from Card import *
from Set import *

class Alchemy(Set):
    def __init__(self):
        Set.__init__(self)

        #Kingdom Cards
        self.kingdomCards.append(Card('Alchemist', 'kingdom', 'Alchemy', 3, 1))
        self.kingdomCards.append(Card('Apothecary', 'kingdom', 'Alchemy', 2, 1))
        self.kingdomCards.append(Card('Apprentice', 'kingdom', 'Alchemy', 5))
        self.kingdomCards.append(Card('Familiar', 'kingdom', 'Alchemy', 3, 1))
        self.kingdomCards.append(Card('Golem', 'kingdom', 'Alchemy', 4, 1))

        self.kingdomCards.append(Card('Herbalist', 'kingdom', 'Alchemy', 2))
        self.kingdomCards.append(Card('Philosopher\'s Stone', 'kingdom', 'Alchemy', 3, 1))
        self.kingdomCards.append(Card('Possession', 'kingdom', 'Alchemy', 6, 1))
        self.kingdomCards.append(Card('Scrying Pool', 'kingdom', 'Alchemy', 2, 1))
        self.kingdomCards.append(Card('Transmute', 'kingdom', 'Alchemy', 0, 1))

        self.kingdomCards.append(Card('University', 'kingdom', 'Alchemy', 2, 1))
        self.kingdomCards.append(Card('Vineyard', 'kingdom', 'Alchemy', 0, 1))

    def getExtraSupplyCards(self, kingdomCards, eventCards, landmarkCards):
        extraSupplyCards = []

        usingPotion = False
        
        for kingdomCard in kingdomCards:
            if not usingPotion and kingdomCard.potions > 0:
                extraSupplyCards.append(Card('Potion', 'supply', 'Alchemy', 4))
                usingPotion = True

        return extraSupplyCards
