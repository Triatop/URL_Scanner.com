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

        return '/'.join(urlSplit)
    def checkRedirect(self, url): 
        self.short = 0
        try:
            headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.102 Safari/537.36"}
            resp = requests.get(url, headers=headers)
            url = resp.url[:resp.url.rindex('/')+1]
            for h in resp.history:
                if h.status_code >= 300:
                    self.short = 1
                    break
        except:
            pass
        return url
            
    def validateUrl(self, url):
        if(len(url) <= 0): return None

        urlSplit = self.splitUrl(url)
        if('http' not in urlSplit[0]): return None

        try:
            headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.102 Safari/537.36"}
            test = requests.get(url, headers=headers)
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
