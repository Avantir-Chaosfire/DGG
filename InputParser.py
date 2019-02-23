from Constants import *

class InputParser:
    def __init__(self, macros, cardSetEditionNames):
        self.macros = macros
        self.cardSetEditionNames = cardSetEditionNames
        self.setsToUse = {}

    def getSetsToUse(self):
        command = input().lower()
        while self.parseCommand(command):
            command = input().lower()
                
        return self.setsToUse

    def parseCommand(self, command):
        if command in self.macros:
            result = True
            for subCommand in self.macros[command]:
                result = self.parseCommand(subCommand) and result
            return result
        else:
            args = command.split(' ')
            weight = 1

            try:
                weight = int(args[-1])
                args = args[:-1]
            except ValueError:
                pass

            command = ' '.join(args)
            
            if command == Constants.DONE_COMMAND:
                return False
            elif command == Constants.MACROS_COMMAND:
                for macro in self.macros.keys():
                    print('\t' + macro)
                return True
            elif command in self.cardSetEditionNames:
                if command in self.setsToUse:
                    print('Duplicate expansion')
                    return True
                else:
                    (cardSetName, edition) = self.cardSetEditionNames[command]
                    self.setsToUse[cardSetName] = (edition, weight)
                    return True
            else:
                print('Unknown expansion')
                return True
