import cryptography.fernet
import urllib.request
import requests
from socket import gethostbyname

class UrlController:

    def __init__(self):
        self.key = b'pz1Z8gLyrtR4lM7kCqMSv5zUwP3AGFoPtQXprqSvDGA='
        self.f = cryptography.fernet.Fernet(self.key)

    def addProtocol(self, url):
        urlSplit = self.splitUrl(url)
        if(len(urlSplit) <= 0): return None 

        if 'http' not in urlSplit[0]:
            urlSplit.insert(0, 'http:/')
        else:
            urlSplit[0] += '/'

        if 'www' not in urlSplit[1][:3]:
            urlSplit[1] = 'www.' + urlSplit[1]

        return '/'.join(urlSplit)

    def checkRedirect(self, url): 
        self.short = 0
        try:
            resp = urllib.request.urlopen(url)                      
            if resp.url != url:                         
                self.short = 1
            return resp.url
        except:
            return url
            
    def validateUrl(self, url):
        if(len(url) <= 0): return None

        urlSplit = self.splitUrl(url)

        if('http' not in urlSplit[0]): return None

        try:
            test = requests.get(url)
            if not test.ok: return None
        except:
            pass
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