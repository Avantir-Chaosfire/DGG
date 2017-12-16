from Card import *
from Set import *

class Adventures(Set):
    def __init__(self):
        Set.__init__(self)

        #Kingdom Cards
        self.kingdomCards.append(Card('Amulet', 'kingdom', 'Adventures', 3))
        self.kingdomCards.append(Card('Artificer', 'kingdom', 'Adventures', 5))
        self.kingdomCards.append(Card('Bridge Troll', 'kingdom', 'Adventures', 5))
        self.kingdomCards.append(Card('Caravan Guard', 'kingdom', 'Adventures', 3))
        self.kingdomCards.append(Card('Coin of the Realm', 'kingdom', 'Adventures', 2))

        self.kingdomCards.append(Card('Distant Lands', 'kingdom', 'Adventures', 5))
        self.kingdomCards.append(Card('Dungeon', 'kingdom', 'Adventures', 3))
        self.kingdomCards.append(Card('Duplicate', 'kingdom', 'Adventures', 4))
        self.kingdomCards.append(Card('Gear', 'kingdom', 'Adventures', 3))
        self.kingdomCards.append(Card('Giant', 'kingdom', 'Adventures', 5))

        self.kingdomCards.append(Card('Guide', 'kingdom', 'Adventures', 3))
        self.kingdomCards.append(Card('Haunted Woods', 'kingdom', 'Adventures', 5))
        self.kingdomCards.append(Card('Hireling', 'kingdom', 'Adventures', 6))
        self.kingdomCards.append(Card('Lost City', 'kingdom', 'Adventures', 5))
        self.kingdomCards.append(Card('Magpie', 'kingdom', 'Adventures', 4))

        self.kingdomCards.append(Card('Messenger', 'kingdom', 'Adventures', 4))
        self.kingdomCards.append(Card('Miser', 'kingdom', 'Adventures', 4))
        self.kingdomCards.append(Card('Page', 'kingdom', 'Adventures', 2))
        self.kingdomCards.append(Card('Peasant', 'kingdom', 'Adventures', 2))
        self.kingdomCards.append(Card('Port', 'kingdom', 'Adventures', 4))

        self.kingdomCards.append(Card('Ranger', 'kingdom', 'Adventures', 4))
        self.kingdomCards.append(Card('Ratcatcher', 'kingdom', 'Adventures', 2))
        self.kingdomCards.append(Card('Raze', 'kingdom', 'Adventures', 2))
        self.kingdomCards.append(Card('Relic', 'kingdom', 'Adventures', 5))
        self.kingdomCards.append(Card('Royal Carriage', 'kingdom', 'Adventures', 5))

        self.kingdomCards.append(Card('Storyteller', 'kingdom', 'Adventures', 5))
        self.kingdomCards.append(Card('Swamp Hag', 'kingdom', 'Adventures', 5))
        self.kingdomCards.append(Card('Transmogrify', 'kingdom', 'Adventures', 4))
        self.kingdomCards.append(Card('Treasure Trove', 'kingdom', 'Adventures', 5))
        self.kingdomCards.append(Card('Wine Merchant', 'kingdom', 'Adventures', 5))

        #Events
        self.events.append(Card('Alms', 'event', 'Adventures', 0))
        self.events.append(Card('Ball', 'event', 'Adventures', 5))
        self.events.append(Card('Bonfire', 'event', 'Adventures', 3))
        self.events.append(Card('Borrow', 'event', 'Adventures', 0))
        self.events.append(Card('Expedition', 'event', 'Adventures', 3))

        self.events.append(Card('Ferry', 'event', 'Adventures', 3))
        self.events.append(Card('Inheritance', 'event', 'Adventures', 7))
        self.events.append(Card('Lost Arts', 'event', 'Adventures', 6))
        self.events.append(Card('Mission', 'event', 'Adventures', 4))
        self.events.append(Card('Pathfinding', 'event', 'Adventures', 8))

        self.events.append(Card('Pilgrimage', 'event', 'Adventures', 4))
        self.events.append(Card('Plan', 'event', 'Adventures', 3))
        self.events.append(Card('Quest', 'event', 'Adventures', 0))
        self.events.append(Card('Raid', 'event', 'Adventures', 5))
        self.events.append(Card('Save', 'event', 'Adventures', 1))

        self.events.append(Card('Scouting Party', 'event', 'Adventures', 2))
        self.events.append(Card('Seaway', 'event', 'Adventures', 5))
        self.events.append(Card('Trade', 'event', 'Adventures', 5))
        self.events.append(Card('Training', 'event', 'Adventures', 6))
        self.events.append(Card('Travelling Fair', 'event', 'Adventures', 2))

    def getExtraSupplyCards(self, kingdomCards, eventCards, landmarkCards):
        extraSupplyCards = []

        usingTavernMat = False
        usingPlusCardTokens = False
        usingPlusActionTokens = False
        usingPlusBuyTokens = False
        usingPlusCoinTokens = False
        usingJourneyTokens = False
        usingMinusCoinTokens = False
        usingMinusCardTokens = False
        
        for kingdomCard in kingdomCards:
            if kingdomCard.name == 'Page':
                extraSupplyCards.append(Card('Treasure Hunter', 'non-supply', 'Adventures', 3))
                extraSupplyCards.append(Card('Warrior', 'non-supply', 'Adventures', 4))
                extraSupplyCards.append(Card('Hero', 'non-supply', 'Adventures', 5))
                extraSupplyCards.append(Card('Champion', 'non-supply', 'Adventures', 6))
            if kingdomCard.name == 'Peasant':
                extraSupplyCards.append(Card('Solider', 'non-supply', 'Adventures', 3))
                extraSupplyCards.append(Card('Fugitive', 'non-supply', 'Adventures', 4))
                extraSupplyCards.append(Card('Disciple', 'non-supply', 'Adventures', 5))
                extraSupplyCards.append(Card('Teacher', 'non-supply', 'Adventures', 6))
            if not usingTavernMat and kingdomCard.name in ['Coin of the Realm', 'Ratcatcher', 'Guide', 'Duplicate', 'Transmogrify', 'Distant Lands', 'Royal Carriage', 'Wine Merchant', 'Peasant', 'Miser']:
                extraSupplyCards.append(Card('Tavern Mat', 'mats', 'Adventures'))
                usingTavernMat = True
            if not usingPlusCardTokens and kingdomCard.name in ['Peasant', 'Pathfinding']:
                extraSupplyCards.append(Card('+1 Card Tokens', 'tokens', 'Adventures'))
                usingPlusCardTokens = True
            if not usingPlusActionTokens and kingdomCard.name in ['Peasant', 'Lost Arts']:
                extraSupplyCards.append(Card('+1 Action Tokens', 'tokens', 'Adventures'))
                usingPlusActionTokens = True
            if not usingPlusBuyTokens and kingdomCard.name in ['Peasant', 'Seaway']:
                extraSupplyCards.append(Card('+1 Buy Tokens', 'tokens', 'Adventures'))
                usingPlusBuyTokens = True
            if not usingPlusCoinTokens and kingdomCard.name in ['Peasant', 'Training']:
                extraSupplyCards.append(Card('+1 Coin Tokens', 'tokens', 'Adventures'))
                usingPlusCoinTokens = True
            if kingdomCard.name == 'Ferry':
                extraSupplyCards.append(Card('-2 Cost Tokens', 'tokens', 'Adventures'))
            if not usingJourneyTokens and kingdomCard.name in ['Ranger', 'Giant', 'Pilgrimage']:
                extraSupplyCards.append(Card('Journey Tokens', 'tokens', 'Adventures'))
                usingJourneyTokens = True
            if kingdomCard.name == 'Plan':
                extraSupplyCards.append(Card('Trashing Tokens', 'tokens', 'Adventures'))
            if kingdomCard.name == 'Inheritance':
                extraSupplyCards.append(Card('Estate Tokens', 'tokens', 'Adventures'))
            if not usingMinusCoinTokens and kingdomCard.name in ['Bridge Troll', 'Ball']:
                extraSupplyCards.append(Card('-1 Coin Tokens', 'tokens', 'Adventures'))
                usingMinusCoinTokens = True
            if not usingMinusCardTokens and kingdomCard.name in ['Relic', 'Borrow', 'Raid']:
                extraSupplyCards.append(Card('-1 Card Tokens', 'tokens', 'Adventures'))
                usingMinusCardTokens = True

        return extraSupplyCards
