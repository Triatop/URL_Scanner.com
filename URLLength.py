# The average length of the legitimate URL (β) is found to be 40. The average length of the phishing URL (β) is found to be greater than 75.

class LengthURL:
    def __init__(self):
        self.l_URL = ''

    def getData(self, i_URL):
        self.l_URL = i_URL
    def isURLShort(self):   #is it too short? True False    # Risk for false positive ?
        short = 0
        if len(self.l_URL) < 5: #Arbitrary Value
            short = 1
        return short
    def isURLLong(self):    #is it too long? True False     
        long = 0
        if len(self.l_URL) > 54: #Arbitrary Value
            long = 2
        return long
