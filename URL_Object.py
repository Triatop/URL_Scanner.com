import os
from socket import gethostbyname




class URL:
    def __init__(self, i_URL = ''):
        self.u_URL = i_URL


class URL_Object:
    o_URL = URL()
    o_URLLength = 0
    o_URLFavIcon = 0
    o_URLip = ''
    f_bool = False

    def setURL(self, i_URL):
        self.o_URL = i_URL
        return

    def getURL(self):
        return self.o_URL
    
    def setURLLength(self):
        if len(self.o_URL.u_URL) > 100 : #<-- Replace with URL check here 
            self.o_URLLength = 1
        return

    def getURLLength(self):
        return self.o_URLLength

    def set_URLFavIcon(self):
        if self.f_bool == True: # <-- Insert fav icon check here
            self.o_URLFavIcon = 1
        return
    def get_URLFavIcon(self):
        return self.o_URLFavIcon
    def set_URLip(self):                     #Sätt att få ip address
        self.o_URLip = gethostbyname(self.o_URL.u_URL)
        return
    def get_URLip(self):
        return self.o_URLip


#######################################################     SLUT PÅ KLASS    ###################################################################################################################
#######################################################     BÖRJAN PÅ TEST   ###################################################################################################################
url1 = URL('github.com')
u_obj = URL_Object()
u_obj.setURL(url1)

print(u_obj.getURL())
print(u_obj.o_URL.u_URL)

u_obj.setURLLength()
u_obj.set_URLFavIcon()
u_obj.set_URLip()

print('Is URL too long?', u_obj.getURLLength())
print('fav Icon = ', u_obj.get_URLFavIcon())
print('ip Address ', u_obj.get_URLip())


exit
