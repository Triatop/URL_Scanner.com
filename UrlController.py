import serviceping
import cryptography.fernet
import socket

class UrlController:

    def __init__(self):
        self.key = b'pz1Z8gLyrtR4lM7kCqMSv5zUwP3AGFoPtQXprqSvDGA='
        self.f = cryptography.fernet.Fernet(self.key)

    def validateUrl(self, url):

        standardPorts = [443, 80]
        splittedUrl = self.splitUrl(url)
        mainDomain = 0

        if(splittedUrl[0] == 'http:' or splittedUrl[0] == 'https:'):
            mainDomain = 1

        ip : str
        try:
            ip = socket.gethostbyname(splittedUrl[mainDomain])
        except:
            return

        for port in standardPorts:
            try:
                if(serviceping.scan(ip, port)['state'] == 'open'):
                    return True
            except:
                pass
        
        print("Flag that it is run on a weird port")
        return True

    def encryptUrl(self, url):
        return self.f.encrypt(url.encode())
    
    def decrytUrl(self, encryptedMessage):
        return str(self.f.decrypt(encryptedMessage))[2:-1]

    def splitUrl(self, url):
        return list(filter(None, url.split('/')))


# a = UrlController()



# print(a.validateUrl('youtube.com'))

