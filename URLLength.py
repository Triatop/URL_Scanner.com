class LengthURL:
    def __init__(self):
        self.l_URL = ''

    def getData(self, i_URL): #Get the URL
        self.l_URL = i_URL
        return 1

    def isURLLong(self):    #is it too long? True False
        long = False
        if self.URLLong() > 53: #Not Arbitrary Value
            long = True
        return long

    def URLLong(self): #Get URL Length
        return len(self.l_URL)