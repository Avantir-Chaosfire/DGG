class SetDescription:
    def __init__(self, fileName, setName = None):
        self.fileName = fileName
        if setName == None:
            self.setName = fileName
        else:
            self.setName = setName
        self.hasArg = False
        self.arg = 0

    def setArg(self, arg):
        self.arg = arg
        self.hasArg = True
