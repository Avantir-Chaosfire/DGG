from Card import *
from Set import *

class Cornucopia(Set):
    def __init__(self):
        Set.__init__(self)

        #Kingdom Cards
        self.kingdomCards.append(Card('Fairgrounds', 'kingdom', 'Cornucopia', 6))
        self.kingdomCards.append(Card('Farming Village', 'kingdom', 'Cornucopia', 4))
        self.kingdomCards.append(Card('Fortune Teller', 'kingdom', 'Cornucopia', 3))
        self.kingdomCards.append(Card('Hamlet', 'kingdom', 'Cornucopia', 2))
        self.kingdomCards.append(Card('Harvest', 'kingdom', 'Cornucopia', 5))

        self.kingdomCards.append(Card('Horn of Plenty', 'kingdom', 'Cornucopia', 5))
        self.kingdomCards.append(Card('Horse Traders', 'kingdom', 'Cornucopia', 4))
        self.kingdomCards.append(Card('Hunting Party', 'kingdom', 'Cornucopia', 5))
        self.kingdomCards.append(Card('Jester', 'kingdom', 'Cornucopia', 5))
        self.kingdomCards.append(Card('Menagerie', 'kingdom', 'Cornucopia', 3))

        self.kingdomCards.append(Card('Remake', 'kingdom', 'Cornucopia', 4))
        self.kingdomCards.append(Card('Tournament', 'kingdom', 'Cornucopia', 4))
        self.kingdomCards.append(Card('Young Witch', 'kingdom', 'Cornucopia', 4))

    def getExtraSupplyCards(self, kingdomCards, eventCards, landmarkCards):
        extraSupplyCards = []
        
        for kingdomCard in kingdomCards:
            if kingdomCard.name == 'Tournament':
                extraSupplyCards.append(Card('Prizes', 'non-supply', 'Cornucopia', 0))

        return extraSupplyCards
