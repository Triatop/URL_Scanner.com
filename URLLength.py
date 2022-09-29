class LengthURL:
    def __init__(self):
        self.l_URL = ''

    def getData(self, i_URL):
        self.l_URL = i_URL
    def isURLShort(self):   #is it too short? True False
        short = 0
        if len(self.l_URL) < 5: #Arbitrary Value
            short = 1
        return short
    def isURLLong(self):    #is it too long? True False
        long = 0
        if len(self.l_URL) > 100: #Arbitrary Value
            long = 2
        return long




