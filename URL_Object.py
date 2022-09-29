import os
from URLLength import LengthURL
from SiteAge_URL import SiteAge_URL
from Favicon_URL import Favicon_URL
from socket import gethostbyname



class URL_Object:
    o_URL = ''
    o_URLLength = 0
    o_URLFavIcon = False
    o_URLSecureProtocol = False
    o_URLSiteAge = False
    o_isSafe = False
    o_URLip = ''

    def setURL(self, i_URL):
        self.o_URL = i_URL
        return

    def getURL(self):
        return self.o_URL
    
    def setURLLength(self):
        t_len = LengthURL()
        t_len.getData(self.o_URL)
        self.o_URLLength += t_len.isURLShort()
        self.o_URLLength += t_len.isURLLong()
        return

    def getURLLength(self):
        return self.o_URLLength

    def setURLFavIcon(self):
        f_Icon = Favicon_URL()
        if f_Icon.hasFavicon() :# <-- Insert fav icon check here
            self.o_URLFavIcon = True
        return

    def getURLFavIcon(self):
        return self.o_URLFavIcon

    def setURLSecureProtocol(self):
        pass

    def getURLSecureProtocol(self):
        return self.o_URLSecureProtocol

    def setURLSiteAge(self):
        age = SiteAge_URL()
        if age.isInLimit():
            self.o_URLSiteAge = True
        return

    def getURLSiteAge(self):
        return self.o_URLSiteAge

    def setIP(self):                     #Sätt att få ip address
        try :
            self.o_URLip = gethostbyname(self.o_URL)
        except:
            pass
        return

    def getIP(self):
        return self.o_URLip

    def isSafe(self):
        T = 40
        A1 = 0
        A2 = 0
        A3 = 0
        A4 = 0
        if self.o_URLLength != 0:
            A1 = 1
        if self.o_URLFavIcon:
            A2 = 1
        if self.o_URLSecureProtocol:
            A3 = 1
        if self.o_URLSiteAge:
            A4 = 1

        if T - (A1 * 20) - (A2 * 15) - (A3 * 25) - (A4 * 20) > 0 :
            self.o_isSafe = True
        
            return self.o_isSafe


#######################################################     SLUT PÅ KLASS    ###################################################################################################################
#######################################################     BÖRJAN PÅ TEST   ###################################################################################################################
url1 = 'github.com'
u_obj = URL_Object()
u_obj.setURL(url1)

print(u_obj.getURL())
print(u_obj.o_URL)

u_obj.setURLLength()
u_obj.setURLFavIcon()
u_obj.setIP()
u_obj.setURLSecureProtocol()
u_obj.setURLSiteAge()

print('The sites URL is too short(1), too long(2) or ok(0)? ', u_obj.getURLLength())
print('The site has a favicon ', u_obj.getURLFavIcon())
print('The sites IP Address: ', u_obj.getIP())
print('The site has secure protocols: ',u_obj.getURLSecureProtocol())
print('The Site is too young: ',u_obj.getURLSiteAge())
print('The site is safe',u_obj.isSafe()) 

exit