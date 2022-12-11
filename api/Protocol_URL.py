class Protocol_URL():
    def __init__(self):
        self.currentProtocol = ''

    def getData(self, s_prot):
        if (type(s_prot) == list):
            self.currentProtocol = s_prot[0]
        elif (type(s_prot) == str):
            self.currentProtocol = s_prot
        else:
            return 0
        return 1

    def isSecure(self):
        if (self.currentProtocol == "https") :
            return 1
        else :
            return 0
