class Protocol_URL():
    def __init__(self):
        self.secureProtocols = []
        self.currentProtocol = ''

    def getData(self, s_prot):
        if (type(s_prot) == list):
            for i in range (len(s_prot)):
                self.secureProtocols.append(s_prot[i])
            self.currentProtocol = self.secureProtocols[0]
            return 1
        elif (type(s_prot) == str):
            self.secureProtocols.append(s_prot)
            self.currentProtocol = self.secureProtocols[0]
            return 1
        else:
            return 0

    def isSecure(self):
        if (self.currentProtocol == "https") :
            return 1
        else :
            return 0