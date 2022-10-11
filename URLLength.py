# The average length of the legitimate URL (β) is found to be 40. The average length of the phishing URL (β) is found to be greater than 75.

class LengthURL:
    def __init__(self):
        self.l_URL = ''
    def getData(self, i_URL):
        self.l_URL = i_URL
    def isURLLong(self):    #is it too long? True False     
        long = 0
        if len(self.l_URL) > 54: #Suspicious
            long = 1
        if len(self.l_URL) > 75: #Phising
            long = 2
        return long
