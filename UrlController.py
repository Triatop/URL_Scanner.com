import serviceping
import cryptography.fernet
import requests

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

        for port in standardPorts:
            if(serviceping.scan(splittedUrl[mainDomain], port)['state'] == 'open'):
                return True
        
        #Flag that website is on wierd port.
        print(f'The url is hosted on a non-standard port')

        return requests.request(method='GET', url=url).ok

    def encryptUrl(self, url):
        return self.f.encrypt(url.encode())
    
    def decrytUrl(self, encryptedMessage):
        return str(self.f.decrypt(encryptedMessage))[2:-1]

    def splitUrl(self, url):
        return list(filter(None, url.split('/')))


a = UrlController()


print(a.validateUrl('https://stackabuse.com/python-check-if-string-contains-substring/'))

