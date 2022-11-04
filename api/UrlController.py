import cryptography.fernet
import urllib.request
from socket import gethostbyname

class UrlController:

    def __init__(self):
        self.key = b'pz1Z8gLyrtR4lM7kCqMSv5zUwP3AGFoPtQXprqSvDGA='
        self.f = cryptography.fernet.Fernet(self.key)

    def checkRedirect(self, url):                       # must contain http
        self.short = 0
        resp = urllib.request.urlopen(url)
        if resp.getcode() == 200:                       # 404 if 404 error
            if resp.url != url:                         # if not same -> url shortening
                self.short = 1
        return resp.url
            
    def validateUrl(self, url):
        if(len(url) <= 0): return None

        urlSplit = self.splitUrl(url)

        if('http' not in urlSplit[0]): return None

        return self.getIP(urlSplit[1])

    def getIP(self, url):
        try:
            return gethostbyname(url)
        except:
            return None

    def encryptUrl(self, url):
        return self.f.encrypt(url.encode())
    
    def decrytUrl(self, encryptedMessage):
        return str(self.f.decrypt(encryptedMessage))[2:-1]

    def splitUrl(self, url):
        return list(filter(None, url.split('/')))