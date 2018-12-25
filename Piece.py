from Constants import *

class Piece:
    def __init__(self, name, setName, edition, kind, properties):
        self.name = name
        self.setName = setName
        self.edition = edition
        self.kind = kind
        
        self.cost = properties.get(Constants.COST_ATTRIBUTE, Constants.COST_DEFAULT_VALUE)
        self.potions = properties.get(Constants.POTIONS_ATTRIBUTE, Constants.POTIONS_DEFAULT_VALUE)
        self.debt = properties.get(Constants.DEBT_ATTRIBUTE, Constants.DEBT_DEFAULT_VALUE)
        self.requires = properties.get(Constants.REQUIRES_ATTRIBUTE, [])
        self.random = properties.get(Constants.RANDOM_ATTRIBUTE, Constants.RANDOM_DEFAULT_VALUE)
        self.available = properties.get(Constants.AVAILABLE_ATTRIBUTE, Constants.AVAILABLE_DEFAULT_VALUE)
        self.select = properties.get(Constants.SELECT_ATTRIBUTE, Constants.SELECT_DEFAULT_VALUE)
        self.weight = properties.get(Constants.WEIGHT_ATTRIBUTE, Constants.WEIGHT_DEFAULT_VALUE)

        self.recommended = False
        self.selectedBy = []

    def print(self, formatProperties):
        #This disaster is how you turn integers into things like '1st', '2nd', '3rd' etc. while
        #enabling it to work for any integer and not requiring people who use this code to install
        #any libraries. This was developed for a stackexchange codegolf question by Gareth:
        #https://codegolf.stackexchange.com/a/4712
        ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n//10%10!=1)*(n%10<4)*n%10::4])
        
        lengths = formatProperties.lengths[self.kind]
        
        output = '\t'
        if lengths[Constants.COST_ATTRIBUTE] > 0:
            output += str(self.cost)
            targetSize = 0
            costString = ''
            if lengths[Constants.POTIONS_ATTRIBUTE] > 0 and lengths[Constants.DEBT_ATTRIBUTE] > 0:
                targetSize = lengths[Constants.COMBINED_SECONDARY_COST_ATTRIBUTE] + 5
                if self.potions > 0 and self.debt > 0:
                    costString = '(' + str(self.potions) + 'p,' + str(self.debt) + 'd)'
                elif self.potions > 0:
                    costString = '(' + str(self.potions) + 'p)'
                elif self.debt > 0:
                    costString = '(' + str(self.debt) + 'd)'
            elif lengths[Constants.POTIONS_ATTRIBUTE] > 0:
                targetSize = lengths[Constants.POTIONS_ATTRIBUTE] + 3
                costString = '(' + str(self.potions) + 'p)' if self.potions > 0 else ''
            elif lengths[Constants.DEBT_ATTRIBUTE] > 0:
                targetSize = lengths[Constants.DEBT_ATTRIBUTE] + 3
                costString = '(' + str(self.debt) + 'd)' if self.debt > 0 else ''
            if lengths[Constants.POTIONS_ATTRIBUTE] > 0 or lengths[Constants.DEBT_ATTRIBUTE] > 0:
                output += costString + ''.join([' ' for i in range(targetSize - len(costString))])
            output += ' - '
        output += self.name + ' (' + self.setName + ('' if self.edition == 0 else ' ' + ordinal(self.edition) + ' Edition') + ')'
        
        if len(self.selectedBy) > 0:
            output += ' [Selected by: ' + self.selectedBy[0]
            for pieceName in self.selectedBy[1:]:
                output += ', ' + pieceName
            output += ']'
            
        if self.recommended:
            output += ' [Recommended]'
            
        print(output)

        self.recommended = False
        self.selectedBy = []
