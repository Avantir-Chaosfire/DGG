from Card import *
from Set import *

class Nocturne(Set):
    def __init__(self):
        Set.__init__(self)

        #Kingdom Cards
        self.kingdomCards.append(Card('Bard', 'kingdom', 'Nocturne', 4))
        self.kingdomCards.append(Card('Blessed Village', 'kingdom', 'Nocturne', 4))
        self.kingdomCards.append(Card('Cemetery', 'kingdom', 'Nocturne', 4))
        self.kingdomCards.append(Card('Changeling', 'kingdom', 'Nocturne', 3))
        self.kingdomCards.append(Card('Cobbler', 'kingdom', 'Nocturne', 5))

        self.kingdomCards.append(Card('Conclave', 'kingdom', 'Nocturne', 4))
        self.kingdomCards.append(Card('Crypt', 'kingdom', 'Nocturne', 5))
        self.kingdomCards.append(Card('Cursed Village', 'kingdom', 'Nocturne', 5))
        self.kingdomCards.append(Card('Den of Sin', 'kingdom', 'Nocturne', 5))
        self.kingdomCards.append(Card('Devil\'s Workshop', 'kingdom', 'Nocturne', 4))

        self.kingdomCards.append(Card('Druid', 'kingdom', 'Nocturne', 2))
        self.kingdomCards.append(Card('Exorcist', 'kingdom', 'Nocturne', 4))
        self.kingdomCards.append(Card('Faithful Hound', 'kingdom', 'Nocturne', 2))
        self.kingdomCards.append(Card('Fool', 'kingdom', 'Nocturne', 3))
        self.kingdomCards.append(Card('Ghost Town', 'kingdom', 'Nocturne', 3))

        self.kingdomCards.append(Card('Guardian', 'kingdom', 'Nocturne', 2))
        self.kingdomCards.append(Card('Idol', 'kingdom', 'Nocturne', 5))
        self.kingdomCards.append(Card('Leprechaun', 'kingdom', 'Nocturne', 3))
        self.kingdomCards.append(Card('Monastery', 'kingdom', 'Nocturne', 2))
        self.kingdomCards.append(Card('Necromancer', 'kingdom', 'Nocturne', 4))

        self.kingdomCards.append(Card('Night Watchman', 'kingdom', 'Nocturne', 3))
        self.kingdomCards.append(Card('Pixie', 'kingdom', 'Nocturne', 2))
        self.kingdomCards.append(Card('Pooka', 'kingdom', 'Nocturne', 5))
        self.kingdomCards.append(Card('Raider', 'kingdom', 'Nocturne', 6))
        self.kingdomCards.append(Card('Sacred Grove', 'kingdom', 'Nocturne', 5))

        self.kingdomCards.append(Card('Secret Cave', 'kingdom', 'Nocturne', 3))
        self.kingdomCards.append(Card('Shepherd', 'kingdom', 'Nocturne', 4))
        self.kingdomCards.append(Card('Skulk', 'kingdom', 'Nocturne', 4))
        self.kingdomCards.append(Card('Tormentor', 'kingdom', 'Nocturne', 5))
        self.kingdomCards.append(Card('Tracker', 'kingdom', 'Nocturne', 2))

        self.kingdomCards.append(Card('Tragic Hero', 'kingdom', 'Nocturne', 5))
        self.kingdomCards.append(Card('Vampire', 'kingdom', 'Nocturne', 5))
        self.kingdomCards.append(Card('Werewolf', 'kingdom', 'Nocturne', 5))

    def getExtraSupplyCards(self, kingdomCards, eventCards, landmarkCards):
        extraSupplyCards = []

        usingBoons = False
        usingHexes = False
        usingWillOWisp = False
        usingWish = False
        usingImp = False
        usingGhost = False
        
        for kingdomCard in kingdomCards:
            if kingdomCard.name == 'Pixie':
                extraSupplyCards.append(Card('Goat', 'heirlooms', 'Nocturne', 2))
            if kingdomCard.name == 'Tracker':
                extraSupplyCards.append(Card('Pouch', 'heirlooms', 'Nocturne', 2))
            if kingdomCard.name == 'Fool':
                extraSupplyCards.append(Card('Lucky Coin', 'heirlooms', 'Nocturne', 4))
                extraSupplyCards.append(Card('Lost in the Woods', 'state', 'Nocturne'))
            if kingdomCard.name == 'Secret Cave':
                extraSupplyCards.append(Card('Magic Lamp', 'heirlooms', 'Nocturne', 0))
            if kingdomCard.name == 'Cemetery':
                extraSupplyCards.append(Card('Haunted Mirror', 'heirlooms', 'Nocturne', 0))
            if kingdomCard.name == 'Shepherd':
                extraSupplyCards.append(Card('Pasture', 'heirlooms', 'Nocturne', 2))
            if kingdomCard.name == 'Pooka':
                extraSupplyCards.append(Card('Cursed Gold', 'heirlooms', 'Nocturne', 4))
            if not usingBoons and kingdomCard.name in ['Druid', 'Pixie', 'Tracker', 'Fool', 'Bard', 'Blessed Village', 'Idol', 'Sacred Grove']:
                extraSupplyCards.append(Card('Boons', 'effects', 'Nocturne'))
                usingBoons = True
                if not usingWillOWisp:
                    extraSupplyCards.append(Card('Will-o\'-Wisp', 'non-supply', 'Nocturne', 0))
                    usingWillOWisp = True
            if not usingHexes and kingdomCard.name in ['Leprechaun', 'Skulk', 'Cursed Village', 'Tormentor', 'Vampire', 'Werewolf']:
                extraSupplyCards.append(Card('Hexes', 'effects', 'Nocturne'))
                extraSupplyCards.append(Card('Deluded/Envious', 'states', 'Nocturne'))
                extraSupplyCards.append(Card('Miserable/Twice Miserable', 'states', 'Nocturne'))
                usingHexes = True
            if not usingWillOWisp and kingdomCard.name == 'Exorcist':
                extraSupplyCards.append(Card('Will-o\'-Wisp', 'non-supply', 'Nocturne', 0))
                usingWillOWisp = True
            if not usingImp and kingdomCard.name in ['Devil\'s Workshop', 'Tormentor', 'Exorcist']:
                extraSupplyCards.append(Card('Imp', 'non-supply', 'Nocturne', 2))
                usingImp = True
            if not usingGhost and kingdomCard.name in ['Haunted Mirror', 'Exorcist']:
                extraSupplyCards.append(Card('Ghost', 'non-supply', 'Nocturne', 4))
                usingGhost = True
            if not usingWish and kingdomCard.name in ['Leprechaun', 'Secret Cave']:
                extraSupplyCards.append(Card('Wish', 'non-supply', 'Nocturne', 0))
                usingWish = True
            if kingdomCard.name == 'Necromancer':
                extraSupplyCards.append(Card('Zombies', 'trash', 'Nocturne', 3))
            if kingdomCard.name == 'Vampire':
                extraSupplyCards.append(Card('Bat', 'non-supply', 'Nocturne', 2))

        return extraSupplyCards
