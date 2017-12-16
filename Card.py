class Card:
    def __init__(self, name, kind, setName, cost = -1, potions = 0, debt = 0):
        self.name = name
        self.kind = kind
        self.setName = setName
        self.cost = cost
        self.potions = potions
        self.debt = debt
