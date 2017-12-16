class Set:
    def __init__(self):
        self.kingdomCards = []
        self.events = []
        self.landmarks = []

    def getKingdomCards(self):
        return self.kingdomCards

    def getEvents(self):
        return self.events

    def getLandmarks(self):
        return self.landmarks

    def getExtraSupplyCards(self, kingdomCards, eventCards, landmarkCards):
        return []
