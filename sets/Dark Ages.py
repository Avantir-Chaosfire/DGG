from random import *

from Card import *
from Set import *

class DarkAges(Set):
    def __init__(self):
        Set.__init__(self)

        #Kingdom Cards
        self.kingdomCards.append(Card('Altar', 'kingdom', 'Dark Ages', 6))
        self.kingdomCards.append(Card('Armory', 'kingdom', 'Dark Ages', 4))
        self.kingdomCards.append(Card('Band of Misfits', 'kingdom', 'Dark Ages', 5))
        self.kingdomCards.append(Card('Bandit Camp', 'kingdom', 'Dark Ages', 5))
        self.kingdomCards.append(Card('Beggar', 'kingdom', 'Dark Ages', 2))

        self.kingdomCards.append(Card('Catacombs', 'kingdom', 'Dark Ages', 5))
        self.kingdomCards.append(Card('Count', 'kingdom', 'Dark Ages', 5))
        self.kingdomCards.append(Card('Counterfeit', 'kingdom', 'Dark Ages', 5))
        self.kingdomCards.append(Card('Cultist', 'kingdom', 'Dark Ages', 5))
        self.kingdomCards.append(Card('Death Cart', 'kingdom', 'Dark Ages', 4))

        self.kingdomCards.append(Card('Feodum', 'kingdom', 'Dark Ages', 4))
        self.kingdomCards.append(Card('Forager', 'kingdom', 'Dark Ages', 3))
        self.kingdomCards.append(Card('Fortress', 'kingdom', 'Dark Ages', 4))
        self.kingdomCards.append(Card('Graverobber', 'kingdom', 'Dark Ages', 5))
        self.kingdomCards.append(Card('Hermit', 'kingdom', 'Dark Ages', 3))

        self.kingdomCards.append(Card('Hunting Grounds', 'kingdom', 'Dark Ages', 6))
        self.kingdomCards.append(Card('Ironmonger', 'kingdom', 'Dark Ages', 4))
        self.kingdomCards.append(Card('Junk Dealer', 'kingdom', 'Dark Ages', 5))
        self.kingdomCards.append(Card('Knights', 'kingdom', 'Dark Ages', 5))
        self.kingdomCards.append(Card('Marauder', 'kingdom', 'Dark Ages', 4))

        self.kingdomCards.append(Card('Market Square', 'kingdom', 'Dark Ages', 3))
        self.kingdomCards.append(Card('Mystic', 'kingdom', 'Dark Ages', 5))
        self.kingdomCards.append(Card('Pillage', 'kingdom', 'Dark Ages', 5))
        self.kingdomCards.append(Card('Poor House', 'kingdom', 'Dark Ages', 1))
        self.kingdomCards.append(Card('Procession', 'kingdom', 'Dark Ages', 4))

        self.kingdomCards.append(Card('Rats', 'kingdom', 'Dark Ages', 4))
        self.kingdomCards.append(Card('Rebuild', 'kingdom', 'Dark Ages', 5))
        self.kingdomCards.append(Card('Rogue', 'kingdom', 'Dark Ages', 5))
        self.kingdomCards.append(Card('Sage', 'kingdom', 'Dark Ages', 3))
        self.kingdomCards.append(Card('Scavenger', 'kingdom', 'Dark Ages', 4))

        self.kingdomCards.append(Card('Squire', 'kingdom', 'Dark Ages', 2))
        self.kingdomCards.append(Card('Storeroom', 'kingdom', 'Dark Ages', 3))
        self.kingdomCards.append(Card('Urchin', 'kingdom', 'Dark Ages', 3))
        self.kingdomCards.append(Card('Vagrant', 'kingdom', 'Dark Ages', 2))
        self.kingdomCards.append(Card('Wandering Minstrel', 'kingdom', 'Dark Ages', 4))

    def getExtraSupplyCards(self, kingdomCards, eventCards, landmarkCards):
        extraSupplyCards = []

        usingSpoils = False
        usingRuins = False
        darkAgesCardCount = 0
        
        for kingdomCard in kingdomCards:
            if kingdomCard.setName == 'Dark Ages':
                if kingdomCard.name == 'Hermit':
                    extraSupplyCards.append(Card('Madman', 'non-supply', 'Dark Ages', 0))
                if kingdomCard.name == 'Urchin':
                    extraSupplyCards.append(Card('Mercenary', 'non-supply', 'Dark Ages', 0))
                if not usingSpoils and kingdomCard.name in ['Bandit Camp', 'Marauder', 'Pillage']:
                    extraSupplyCards.append(Card('Spoils', 'non-supply', 'Dark Ages', 0))
                    usingSpoils = True
                if not usingRuins and kingdomCard.name in ['Cultist', 'Death Cart', 'Marauder']:
                    extraSupplyCards.append(Card('Ruins', 'non-supply', 'Dark Ages', 0))
                    usingRuins = True

                darkAgesCardCount += 1

        if randint(0, 9) < darkAgesCardCount:
            extraSupplyCards.append(Card('Shelters', 'starting estates', 'Dark Ages', 1))

        return extraSupplyCards
