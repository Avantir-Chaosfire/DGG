from random import *

from Card import *
from Set import *

class Prosperity(Set):
    def __init__(self):
        Set.__init__(self)

        #Kingdom Cards
        self.kingdomCards.append(Card('Bank', 'kingdom', 'Prosperity', 7))
        self.kingdomCards.append(Card('Bishop', 'kingdom', 'Prosperity', 4))
        self.kingdomCards.append(Card('City', 'kingdom', 'Prosperity', 5))
        self.kingdomCards.append(Card('Contraband', 'kingdom', 'Prosperity', 5))
        self.kingdomCards.append(Card('Counting House', 'kingdom', 'Prosperity', 5))

        self.kingdomCards.append(Card('Expand', 'kingdom', 'Prosperity', 7))
        self.kingdomCards.append(Card('Forge', 'kingdom', 'Prosperity', 7))
        self.kingdomCards.append(Card('Goons', 'kingdom', 'Prosperity', 6))
        self.kingdomCards.append(Card('Grand Market', 'kingdom', 'Prosperity', 6))
        self.kingdomCards.append(Card('Hoard', 'kingdom', 'Prosperity', 6))

        self.kingdomCards.append(Card('King\'s Court', 'kingdom', 'Prosperity', 7))
        self.kingdomCards.append(Card('Loan', 'kingdom', 'Prosperity', 3))
        self.kingdomCards.append(Card('Mint', 'kingdom', 'Prosperity', 5))
        self.kingdomCards.append(Card('Monument', 'kingdom', 'Prosperity', 4))
        self.kingdomCards.append(Card('Mountebank', 'kingdom', 'Prosperity', 5))

        self.kingdomCards.append(Card('Peddler', 'kingdom', 'Prosperity', 8))
        self.kingdomCards.append(Card('Quarry', 'kingdom', 'Prosperity', 4))
        self.kingdomCards.append(Card('Rabble', 'kingdom', 'Prosperity', 5))
        self.kingdomCards.append(Card('Royal Seal', 'kingdom', 'Prosperity', 5))
        self.kingdomCards.append(Card('Talisman', 'kingdom', 'Prosperity', 4))

        self.kingdomCards.append(Card('Trade Route', 'kingdom', 'Prosperity', 3))
        self.kingdomCards.append(Card('Vault', 'kingdom', 'Prosperity', 5))
        self.kingdomCards.append(Card('Venture', 'kingdom', 'Prosperity', 5))
        self.kingdomCards.append(Card('Watchtower', 'kingdom', 'Prosperity', 3))
        self.kingdomCards.append(Card('Worker\'s Village', 'kingdom', 'Prosperity', 4))

    def getExtraSupplyCards(self, kingdomCards, eventCards, landmarkCards):
        extraSupplyCards = []

        usingVictoryMat = False
        prosperityCardCount = 0
        
        for kingdomCard in kingdomCards:
            if kingdomCard.setName == 'Prosperity':
                if not usingVictoryMat and kingdomCard.name in ['Bishop', 'Goons', 'Monument']:
                    extraSupplyCards.append(Card('Victory Token Mat (Optional)', 'mats', 'Prosperity'))
                    extraSupplyCards.append(Card('Victory Tokens', 'tokens', 'Prosperity'))
                    usingVictoryMat = True
                if kingdomCard.name == 'Trade Route':
                    extraSupplyCards.append(Card('Trade Route Mat', 'mats', 'Prosperity'))
                    extraSupplyCards.append(Card('Coin Tokens', 'tokens', 'Prosperity'))

                prosperityCardCount += 1

        if randint(0, 9) < prosperityCardCount:
            extraSupplyCards.append(Card('Platinum', 'supply', 'Prosperity', 9))
            extraSupplyCards.append(Card('Colony', 'supply', 'Prosperity', 11))

        return extraSupplyCards
