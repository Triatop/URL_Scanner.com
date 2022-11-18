from urllib.parse import urlparse


class SpecialCharactersCheck:
    def __init__(self):
        self.l_URL = ''
        self.sev = 0

    def setData(self, i_URL):
        self.l_URL = i_URL
        return 1

    def processData(self):                  
        sign = '-'
        domain = urlparse(self.l_URL).netloc
        for c in domain:
            if c == sign:
                self.sev = 1
        domain = urlparse(self.l_URL).hostname
        domain = domain.replace('www.', '')
        if domain.count('.') > 2:
            self.sev = 2
        sign = '@'
        for c in self.l_URL:
            if c == sign:
                self.sev = 3
        sign = '/'
        for i in range(7, len(self.l_URL)-1):
            if self.l_URL[i] == self.l_URL[i+1]:
                if self.l_URL[i] == sign:
                    self.sev = 4
        return self.sev
