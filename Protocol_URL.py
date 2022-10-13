class Protocol_URL():
    def __init__(self):
        self.secureProtocols = []
        self.currentProtocol = ''

    def getData(self, s_prot):
        self.secureProtocols.append(s_prot)
        self.currentProtocol = self.secureProtocols[0]

    def isSecure(self):
        if (self.currentProtocol == "https") :
            return True
        else :
            return False