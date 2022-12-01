import cryptography.fernet
import requests
from socket import gethostbyname

class UrlController:

    def __init__(self):
        self.key = b'pz1Z8gLyrtR4lM7kCqMSv5zUwP3AGFoPtQXprqSvDGA='
        self.f = cryptography.fernet.Fernet(self.key)

    def addProtocol(self, url):
        if(len(url) == 0): return '' 
        urlSplit = self.splitUrl(url)

        if 'http' not in urlSplit[0]:
            urlSplit.insert(0, 'http://')
        else:
            urlSplit[0] += '://'

        return ''.join(urlSplit)
    
    def checkRedirect(self, url): 
        try:
            headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.102 Safari/537.36"}
            resp = requests.get(url, headers=headers)
            url = resp.url[:resp.url.rindex('/')+1]
        except:
            pass
        return url
            
    def validateUrl(self, url):
        if(len(url) == 0): return False
        try:
            headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.102 Safari/537.36"}
            test = requests.get(url, headers=headers)
            if not test.ok: return False
        except:
            pass
        return True

    def getIP(self, url):
        try:
            return gethostbyname(list(filter(None, url.split('/')))[1])
        except:
            return None

    def encryptUrl(self, url): #encryption for the database
        return str(self.f.encrypt(url.encode()), encoding='utf-8')
    
    def decryptUrl(self, encryptedMessage): #encryption for the database
        return str(self.f.decrypt(bytes(encryptedMessage, encoding='utf-8')))[2:-1]

    def splitUrl(self, url):
        return url.split('://')
