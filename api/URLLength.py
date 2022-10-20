class LengthURL:
    def __init__(self):
        self.l_URL = ''

    def getData(self, i_URL): #Get the URL
        self.l_URL = i_URL
        return 1

    def isURLLong(self):    #is it too long? 0, 1, 2
        long = 0
        l_url = self.URLLong()
        if l_url > 74: #Not Arbitrary Value
            long = 2
        elif l_url > 53:
            long = 1
        return long

    def URLLong(self): #Get URL Length
        return len(self.l_URL)
