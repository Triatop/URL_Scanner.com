import cryptography.fernet
import socket
from socket import gethostbyname

class UrlController:

    def __init__(self):
        self.key = b'pz1Z8gLyrtR4lM7kCqMSv5zUwP3AGFoPtQXprqSvDGA='
        self.f = cryptography.fernet.Fernet(self.key)

    def validateUrl(self, url):

        # standardPorts = [443, 80]

        urlSplit = self.splitUrl(url)

        if('http' not in urlSplit[0]): return False

        return self.getIP(urlSplit[1]) is not None
        # if not ip: return False

        # for port in standardPorts:
        #     try:
        #         if(serviceping.scan(ip, port)['state'] == 'open'):
        #             return True
        #     except:
        #         pass
        
        # print("Flag that it is run on a weird port")
        # return requests.get(urlSplit[mainDomain]).ok

    def getIP(self, url):
        try:
            return gethostbyname(url)
        except socket.error:
            return None

        
        

    def encryptUrl(self, url):
        return self.f.encrypt(url.encode())
    
    def decrytUrl(self, encryptedMessage):
        return str(self.f.decrypt(encryptedMessage))[2:-1]

    def splitUrl(self, url):
        return list(filter(None, url.split('/')))



# a = UrlController()



# print(a.validateUrl('https://www.youtube.com/watch?v=jezczH06R2g'))

