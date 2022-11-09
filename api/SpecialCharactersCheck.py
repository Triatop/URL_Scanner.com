from urllib.parse import urlparse

class SCCheck:
    def __init__(self):
        self.l_URL = ''
        self.value = 0                      # Amount of bad special charachters

    def setData(self, i_URL):               # Get the URL
        self.l_URL = i_URL
        return 1

    def checkAtSign(self):                  # Url having "@" symbol -> Phising
        sign = '@'
        for c in self.l_URL:
            if c == sign:
                self.value += 1
                return True
        return False

    def checkHyphen(self):                  # Domain name part includes "-" -> Phishing
        sign = '-'
        domain = urlparse(self.l_URL).netloc
        for c in domain:
            if c == sign:
                self.value += 1
                return True
        return False

    def checkDoubleForwardSlash(self):      # The position of the last occurrence of "//" in the URL > 7 -> Phising
        sign = '/'
        for i in range(7, len(self.l_URL)-1):
            if self.l_URL[i] == self.l_URL[i+1]:
                if self.l_URL[i] == sign:
                    self.value += 1
                    return True
        return False

