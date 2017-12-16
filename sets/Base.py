from Card import *
from Set import *

class Base(Set):
    def __init__(self, edition = 2):
        Set.__init__(self)

        #Kingdom Cards
        self.kingdomCards.append(Card('Bureaucrat', 'kingdom', 'Base Set', 4))
        self.kingdomCards.append(Card('Cellar', 'kingdom', 'Base Set', 2))
        self.kingdomCards.append(Card('Chapel', 'kingdom', 'Base Set', 2))
        self.kingdomCards.append(Card('Council Room', 'kingdom', 'Base Set', 5))
        self.kingdomCards.append(Card('Festival', 'kingdom', 'Base Set', 5))
        
        self.kingdomCards.append(Card('Gardens', 'kingdom', 'Base Set', 4))
        self.kingdomCards.append(Card('Laboratory', 'kingdom', 'Base Set', 5))
        self.kingdomCards.append(Card('Library', 'kingdom', 'Base Set', 5))
        self.kingdomCards.append(Card('Market', 'kingdom', 'Base Set', 5))
        self.kingdomCards.append(Card('Militia', 'kingdom', 'Base Set', 4))

        self.kingdomCards.append(Card('Mine', 'kingdom', 'Base Set', 5))
        self.kingdomCards.append(Card('Moat', 'kingdom', 'Base Set', 2))
        self.kingdomCards.append(Card('Moneylender', 'kingdom', 'Base Set', 4))
        self.kingdomCards.append(Card('Remodel', 'kingdom', 'Base Set', 4))
        self.kingdomCards.append(Card('Smithy', 'kingdom', 'Base Set', 4))
                                 
        self.kingdomCards.append(Card('Throne Room', 'kingdom', 'Base Set', 4))
        self.kingdomCards.append(Card('Village', 'kingdom', 'Base Set', 3))
        self.kingdomCards.append(Card('Witch', 'kingdom', 'Base Set', 5))
        self.kingdomCards.append(Card('Workshop', 'kingdom', 'Base Set', 3))

        if edition in [0, 1]:
            self.kingdomCards.append(Card('Adventurer', 'kingdom', 'Base Set (1ed)', 6))
            self.kingdomCards.append(Card('Chancellor', 'kingdom', 'Base Set (1ed)', 3))
            self.kingdomCards.append(Card('Feast', 'kingdom', 'Base Set (1ed)', 4))
            self.kingdomCards.append(Card('Spy', 'kingdom', 'Base Set (1ed)', 4))
            self.kingdomCards.append(Card('Thief', 'kingdom', 'Base Set (1ed)', 4))
            
            self.kingdomCards.append(Card('Woodcutter', 'kingdom', 'Base Set (1ed)', 3))

        if edition in [0, 2]:
            self.kingdomCards.append(Card('Artisan', 'kingdom', 'Base Set (2ed)', 6))
            self.kingdomCards.append(Card('Bandit', 'kingdom', 'Base Set (2ed)', 5))
            self.kingdomCards.append(Card('Harbinger', 'kingdom', 'Base Set (2ed)', 3))
            self.kingdomCards.append(Card('Merchant', 'kingdom', 'Base Set (2ed)', 3))
            self.kingdomCards.append(Card('Poacher', 'kingdom', 'Base Set (2ed)', 4))
            
            self.kingdomCards.append(Card('Sentry', 'kingdom', 'Base Set (2ed)', 5))
            self.kingdomCards.append(Card('Vassal', 'kingdom', 'Base Set (2ed)', 3))
