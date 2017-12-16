from Card import *
from Set import *

class Intrigue(Set):
    def __init__(self, edition = 2):
        Set.__init__(self)

        #Kingdom Cards
        self.kingdomCards.append(Card('Baron', 'kingdom', 'Intrigue', 4))
        self.kingdomCards.append(Card('Bridge', 'kingdom', 'Intrigue', 4))
        self.kingdomCards.append(Card('Conspirator', 'kingdom', 'Intrigue', 4))
        self.kingdomCards.append(Card('Courtyard', 'kingdom', 'Intrigue', 2))
        self.kingdomCards.append(Card('Duke', 'kingdom', 'Intrigue', 5))
        
        self.kingdomCards.append(Card('Harem', 'kingdom', 'Intrigue', 6))
        self.kingdomCards.append(Card('Ironworks', 'kingdom', 'Intrigue', 4))
        self.kingdomCards.append(Card('Masquerade', 'kingdom', 'Intrigue', 3))
        self.kingdomCards.append(Card('Nobles', 'kingdom', 'Intrigue', 6))
        self.kingdomCards.append(Card('Mining Village', 'kingdom', 'Intrigue', 4))
        
        self.kingdomCards.append(Card('Minion', 'kingdom', 'Intrigue', 5))
        self.kingdomCards.append(Card('Pawn', 'kingdom', 'Intrigue', 2))
        self.kingdomCards.append(Card('Shanty Town', 'kingdom', 'Intrigue', 3))
        self.kingdomCards.append(Card('Steward', 'kingdom', 'Intrigue', 3))
        self.kingdomCards.append(Card('Swindler', 'kingdom', 'Intrigue', 3))
        
        self.kingdomCards.append(Card('Torturer', 'kingdom', 'Intrigue', 5))
        self.kingdomCards.append(Card('Trading Post', 'kingdom', 'Intrigue', 5))
        self.kingdomCards.append(Card('Upgrade', 'kingdom', 'Intrigue', 5))
        self.kingdomCards.append(Card('Wishing Well', 'kingdom', 'Intrigue', 3))

        if edition in [0, 1]:
            self.kingdomCards.append(Card('Coppersmith', 'kingdom', 'Intrigue (1ed)', 4))
            self.kingdomCards.append(Card('Great Hall', 'kingdom', 'Intrigue (1ed)', 4))
            self.kingdomCards.append(Card('Saboteur', 'kingdom', 'Intrigue (1ed)', 5))
            self.kingdomCards.append(Card('Scout', 'kingdom', 'Intrigue (1ed)', 4))
            self.kingdomCards.append(Card('Secret Chamber', 'kingdom', 'Intrigue (1ed)', 2))

            self.kingdomCards.append(Card('Tribute', 'kingdom', 'Intrigue (1ed)', 5))

        if edition in [0, 2]:
            self.kingdomCards.append(Card('Courtier', 'kingdom', 'Intrigue (2ed)', 5))
            self.kingdomCards.append(Card('Diplomat', 'kingdom', 'Intrigue (2ed)', 4))
            self.kingdomCards.append(Card('Lurker', 'kingdom', 'Intrigue (2ed)', 2))
            self.kingdomCards.append(Card('Mill', 'kingdom', 'Intrigue (2ed)', 4))
            self.kingdomCards.append(Card('Patrol', 'kingdom', 'Intrigue (2ed)', 5))
            
            self.kingdomCards.append(Card('Replace', 'kingdom', 'Intrigue (2ed)', 5))
            self.kingdomCards.append(Card('Secret Pasage', 'kingdom', 'Intrigue (2ed)', 4))
