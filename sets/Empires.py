from Card import *
from Set import *

class Empires(Set):
    def __init__(self):
        Set.__init__(self)

        #Kingdom Cards
        self.kingdomCards.append(Card('Archive', 'kingdom', 'Empires', 5))
        self.kingdomCards.append(Card('Capital', 'kingdom', 'Empires', 5))
        self.kingdomCards.append(Card('Castles', 'kingdom', 'Empires', 3))
        self.kingdomCards.append(Card('Catapult/Rocks', 'kingdom', 'Empires', 3))
        self.kingdomCards.append(Card('Chariot Race', 'kingdom', 'Empires', 3))
        
        self.kingdomCards.append(Card('Charm', 'kingdom', 'Empires', 5))
        self.kingdomCards.append(Card('City Quarter', 'kingdom', 'Empires', 0, 0, 8))
        self.kingdomCards.append(Card('Crown', 'kingdom', 'Empires', 5))
        self.kingdomCards.append(Card('Encampment/Plunder', 'kingdom', 'Empires', 2))
        self.kingdomCards.append(Card('Enchantress', 'kingdom', 'Empires', 3))
        
        self.kingdomCards.append(Card('Engineer', 'kingdom', 'Empires', 0, 0, 4))
        self.kingdomCards.append(Card('Farmers\' Market', 'kingdom', 'Empires', 3))
        self.kingdomCards.append(Card('Forum', 'kingdom', 'Empires', 5))
        self.kingdomCards.append(Card('Gladiator/Fortune', 'kingdom', 'Empires', 3))
        self.kingdomCards.append(Card('Groundskeeper', 'kingdom', 'Empires', 5))
        
        self.kingdomCards.append(Card('Legionary', 'kingdom', 'Empires', 5))
        self.kingdomCards.append(Card('Overlord', 'kingdom', 'Empires', 0, 0, 8))
        self.kingdomCards.append(Card('Patrician/Emporium', 'kingdom', 'Empires', 2))
        self.kingdomCards.append(Card('Royal Blacksmith', 'kingdom', 'Empires', 0, 0, 8))
        self.kingdomCards.append(Card('Sacrifice', 'kingdom', 'Empires', 4))
        
        self.kingdomCards.append(Card('Settlers/Bustling Village', 'kingdom', 'Empires', 2))
        self.kingdomCards.append(Card('Temple', 'kingdom', 'Empires', 4))
        self.kingdomCards.append(Card('Villa', 'kingdom', 'Empires', 4))
        self.kingdomCards.append(Card('Wild Hunt', 'kingdom', 'Empires', 5))

        #Events
        self.events.append(Card('Advance', 'event', 'Empires', 0))
        self.events.append(Card('Annex', 'event', 'Empires', 0, 0, 8))
        self.events.append(Card('Banquet', 'event', 'Empires', 3))
        self.events.append(Card('Conquest', 'event', 'Empires', 6))
        self.events.append(Card('Delve', 'event', 'Empires', 2))

        self.events.append(Card('Dominate', 'event', 'Empires', 14))
        self.events.append(Card('Donate', 'event', 'Empires', 0, 0, 8))
        self.events.append(Card('Ritual', 'event', 'Empires', 4))
        self.events.append(Card('Salt the Earth', 'event', 'Empires', 4))
        self.events.append(Card('Tax', 'event', 'Empires', 2))

        self.events.append(Card('Triumph', 'event', 'Empires', 0, 0, 5))
        self.events.append(Card('Wedding', 'event', 'Empires', 4, 0, 3))
        self.events.append(Card('Windfall', 'event', 'Empires', 5))

        #Landmarks
        self.landmarks.append(Card('Aqueduct', 'landmark', 'Empires'))
        self.landmarks.append(Card('Arena', 'landmark', 'Empires'))
        self.landmarks.append(Card('Bandit Fort', 'landmark', 'Empires'))
        self.landmarks.append(Card('Basilica', 'landmark', 'Empires'))
        self.landmarks.append(Card('Baths', 'landmark', 'Empires'))

        self.landmarks.append(Card('Battlefield', 'landmark', 'Empires'))
        self.landmarks.append(Card('Colonnade', 'landmark', 'Empires'))
        self.landmarks.append(Card('Defiled Shrine', 'landmark', 'Empires'))
        self.landmarks.append(Card('Fountain', 'landmark', 'Empires'))
        self.landmarks.append(Card('Keep', 'landmark', 'Empires'))

        self.landmarks.append(Card('Labyrinth', 'landmark', 'Empires'))
        self.landmarks.append(Card('Mountain Pass', 'landmark', 'Empires'))
        self.landmarks.append(Card('Museum', 'landmark', 'Empires'))
        self.landmarks.append(Card('Obelisk', 'landmark', 'Empires'))
        self.landmarks.append(Card('Orchard', 'landmark', 'Empires'))

        self.landmarks.append(Card('Palace', 'landmark', 'Empires'))
        self.landmarks.append(Card('Tomb', 'landmark', 'Empires'))
        self.landmarks.append(Card('Tower', 'landmark', 'Empires'))
        self.landmarks.append(Card('Triumphal Arch', 'landmark', 'Empires'))
        self.landmarks.append(Card('Wall', 'landmark', 'Empires'))

        self.landmarks.append(Card('Wolf Den', 'landmark', 'Empires'))

    def getExtraSupplyCards(self, kingdomCards, eventCards, landmarkCards):
        extraSupplyCards = []

        usingVictoryTokens = False
        usingDebtTokens = False
        
        for card in kingdomCards + eventCards:
            if not usingVictoryTokens and card.name in ['Triumph', 'Chariot Race', 'Farmers\' Market', 'Castles', 'Ritual', 'Sacrifice', 'Salt the Earth', 'Temple', 'Wedding', 'Patrician/Emporium', 'Groundskeeper', 'Plunder', 'Wild Hunt', 'Conquest', 'Dominate', 'Aqueduct', 'Arena', 'Basilica', 'Baths', 'Battlefield', 'Colonnade', 'Defiled Shrine', 'Labyrinth', 'Mountain Pass', 'Tomb']:
                extraSupplyCards.append(Card('Victory Tokens', 'tokens', 'Empires'))
                usingVictoryTokens = True
            if not usingDebtTokens and card.name in ['Engineer', 'Triumph', 'Annex', 'City Quarter', 'Donate', 'Overlord', 'Royal Blacksmith', 'Wedding', 'Gladiator/Fortune', 'Mountain Pass']:
                extraSupplyCards.append(Card('Debt Tokens', 'tokens', 'Empires'))
                usingDebtTokens = True

        return extraSupplyCards
