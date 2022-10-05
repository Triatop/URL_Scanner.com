class Protocol_URL(object):
    def __init__(self):
        self.secureProtocols = []
        self,currentProtocol = ''

    def getData(self, s_prot):
        self.secureProtocols = s_prot
        self.currentProt = self.secureProtocols[0]

    def isSecure(self):
        if (self.currentProt == 'https') :
            return True
        else :
            return False