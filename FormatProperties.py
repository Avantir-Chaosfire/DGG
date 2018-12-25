from Constants import *

class FormatProperties:
    def __init__(self):
        self.lengths = {}

    def add(self, piece):
        if piece.kind not in self.lengths:
            self.lengths[piece.kind] = {}

        costs = [
            (piece.cost, Constants.COST_ATTRIBUTE, Constants.COST_DEFAULT_VALUE),
            (piece.potions, Constants.POTIONS_ATTRIBUTE, Constants.POTIONS_DEFAULT_VALUE),
            (piece.debt, Constants.DEBT_ATTRIBUTE, Constants.DEBT_DEFAULT_VALUE)
        ]
                
        for (value, lengthProperty, default) in costs:
            length = 0 if value == default else len(str(value))
            self.lengths[piece.kind][lengthProperty] = max(self.lengths[piece.kind].get(lengthProperty, 0), length)
        self.lengths[piece.kind][Constants.COMBINED_SECONDARY_COST_ATTRIBUTE] = max(self.lengths[piece.kind].get(Constants.COMBINED_SECONDARY_COST_ATTRIBUTE, 0), len(str(piece.potions)) + len(str(piece.debt)))
