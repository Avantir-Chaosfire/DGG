class Piece:
    def __init__(self, name, setName, edition, kind, properties):
        self.name = name
        self.setName = setName
        self.edition = edition
        self.kind = kind
        
        self.cost = properties.get('cost', None)
        self.potions = properties.get('potions', 0)
        self.debt = properties.get('debt', 0)
        self.requires = properties.get('requires', [])
        self.random = properties.get('random', False)
        self.available = properties.get('available', True)
        self.select = properties.get('select', False)
        self.weight = properties.get('weight', None)

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
        if lengths['cost'] > 0:
            output += str(self.cost)
            targetSize = 0
            costString = ''
            if lengths['potions'] > 0 and lengths['debt'] > 0:
                targetSize = lengths['combined'] + 5
                if self.potions > 0 and self.debt > 0:
                    costString = '(' + str(self.potions) + 'p,' + str(self.debt) + 'd)'
                elif self.potions > 0:
                    costString = '(' + str(self.potions) + 'p)'
                elif self.debt > 0:
                    costString = '(' + str(self.debt) + 'd)'
            elif lengths['potions'] > 0:
                targetSize = lengths['potions'] + 3
                costString = '(' + str(self.potions) + 'p)' if self.potions > 0 else ''
            elif lengths['debt'] > 0:
                targetSize = lengths['debt'] + 3
                costString = '(' + str(self.debt) + 'd)' if self.debt > 0 else ''
            if lengths['potions'] > 0 or lengths['debt'] > 0:
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
