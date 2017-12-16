from Card import *
from Set import *

class Hinterlands(Set):
    def __init__(self):
        Set.__init__(self)

        #Kingdom Cards
        self.kingdomCards.append(Card('Border Village', 'kingdom', 'Hinterlands', 6))
        self.kingdomCards.append(Card('Cache', 'kingdom', 'Hinterlands', 5))
        self.kingdomCards.append(Card('Cartographer', 'kingdom', 'Hinterlands', 5))
        self.kingdomCards.append(Card('Crossroads', 'kingdom', 'Hinterlands', 2))
        self.kingdomCards.append(Card('Develop', 'kingdom', 'Hinterlands', 3))

        self.kingdomCards.append(Card('Duchess', 'kingdom', 'Hinterlands', 2))
        self.kingdomCards.append(Card('Embassy', 'kingdom', 'Hinterlands', 5))
        self.kingdomCards.append(Card('Farmland', 'kingdom', 'Hinterlands', 6))
        self.kingdomCards.append(Card('Fool\'s Gold', 'kingdom', 'Hinterlands', 2))
        self.kingdomCards.append(Card('Haggler', 'kingdom', 'Hinterlands', 5))

        self.kingdomCards.append(Card('Highway', 'kingdom', 'Hinterlands', 5))
        self.kingdomCards.append(Card('Ill-Gotten Gains', 'kingdom', 'Hinterlands', 5))
        self.kingdomCards.append(Card('Inn', 'kingdom', 'Hinterlands', 5))
        self.kingdomCards.append(Card('Jack of all Trades', 'kingdom', 'Hinterlands', 4))
        self.kingdomCards.append(Card('Mandarin', 'kingdom', 'Hinterlands', 5))

        self.kingdomCards.append(Card('Margrave', 'kingdom', 'Hinterlands', 5))
        self.kingdomCards.append(Card('Noble Brigand', 'kingdom', 'Hinterlands', 4))
        self.kingdomCards.append(Card('Nomad Camp', 'kingdom', 'Hinterlands', 4))
        self.kingdomCards.append(Card('Oasis', 'kingdom', 'Hinterlands', 3))
        self.kingdomCards.append(Card('Oracle', 'kingdom', 'Hinterlands', 3))

        self.kingdomCards.append(Card('Scheme', 'kingdom', 'Hinterlands', 3))
        self.kingdomCards.append(Card('Silk Road', 'kingdom', 'Hinterlands', 4))
        self.kingdomCards.append(Card('Spice Merchant', 'kingdom', 'Hinterlands', 4))
        self.kingdomCards.append(Card('Stables', 'kingdom', 'Hinterlands', 5))
        self.kingdomCards.append(Card('Trader', 'kingdom', 'Hinterlands', 4))

        self.kingdomCards.append(Card('Tunnel', 'kingdom', 'Hinterlands', 3))
