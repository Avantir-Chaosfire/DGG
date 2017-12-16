from Card import *
from Set import *

class Guilds(Set):
    def __init__(self):
        Set.__init__(self)

        #Kingdom Cards
        self.kingdomCards.append(Card('Advisor', 'kingdom', 'Guilds', 4))
        self.kingdomCards.append(Card('Baker', 'kingdom', 'Guilds', 5))
        self.kingdomCards.append(Card('Butcher', 'kingdom', 'Guilds', 5))
        self.kingdomCards.append(Card('Candlestick Maker', 'kingdom', 'Guilds', 2))
        self.kingdomCards.append(Card('Doctor', 'kingdom', 'Guilds', 3))

        self.kingdomCards.append(Card('Herald', 'kingdom', 'Guilds', 4))
        self.kingdomCards.append(Card('Journeyman', 'kingdom', 'Guilds', 5))
        self.kingdomCards.append(Card('Masterpiece', 'kingdom', 'Guilds', 3))
        self.kingdomCards.append(Card('Merchant Guild', 'kingdom', 'Guilds', 5))
        self.kingdomCards.append(Card('Plaza', 'kingdom', 'Guilds', 4))

        self.kingdomCards.append(Card('Soothsayer', 'kingdom', 'Guilds', 5))
        self.kingdomCards.append(Card('Stonemason', 'kingdom', 'Guilds', 2))
        self.kingdomCards.append(Card('Taxman', 'kingdom', 'Guilds', 4))

    def getExtraSupplyCards(self, kingdomCards, eventCards, landmarkCards):
        extraSupplyCards = []

        usingCoinTokens = False
        
        for kingdomCard in kingdomCards:
            if not usingCoinTokens and kingdomCard.name in ['Candlestick Maker', 'Plaza', 'Baker', 'Butcher', 'Merhcant Guild']:
                extraSupplyCards.append(Card('Coin Tokens', 'tokens', 'Guilds'))
                usingCoinTokens = True

        return extraSupplyCards
