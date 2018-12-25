class FormatProperties:
    def __init__(self):
        self.lengths = {}

    def add(self, piece):
        if piece.kind not in self.lengths:
            self.lengths[piece.kind] = {}
                
        for (value, lengthProperty, default) in [(piece.cost, 'cost', None), (piece.potions, 'potions', 0), (piece.debt, 'debt', 0)]:
            length = 0 if value == default else len(str(value))
            self.lengths[piece.kind][lengthProperty] = max(self.lengths[piece.kind].get(lengthProperty, 0), length)
        self.lengths[piece.kind]['combined'] = max(self.lengths[piece.kind].get('combined', 0), len(str(piece.potions)) + len(str(piece.debt)))
