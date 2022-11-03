class URL_Object:
    def __init__(self) :
        self.o_URL = ''
        self.o_URLLength = 0
        self.o_URLFavIcon = 0
        self.o_URLSecureProtocol = 0
        self.o_URLSiteAge = None
        self.o_isSafe = 0
        self.o_URLip = ''

    def setURL(self, i_URL):
        self.o_URL = i_URL
        return

    def getURL(self):
        return self.o_URL
    
    def setURLLength(self, l_url):
        self.o_URLLength = l_url
        return

    def getURLLength(self):
        return self.o_URLLength

    def setURLFavIcon(self, f_ic):
        self.o_URLFavIcon = f_ic
        return

    def getURLFavIcon(self):
        return self.o_URLFavIcon

    def setURLSecureProtocol(self,s_prot):
        self.o_URLSecureProtocol = s_prot
        return

    def getURLSecureProtocol(self):
        return self.o_URLSecureProtocol

    def setURLSiteAge(self, u_old):
        self.o_URLSiteAge = u_old
        return

    def getURLSiteAge(self):
        return self.o_URLSiteAge

    def setIP(self, u_ip):                     
        self.o_URLip = u_ip
        return

    def getIP(self):
        return self.o_URLip

    def setSafe(self, i_safe):
        self.o_isSafe = i_safe
        return

    def getSafe(self):
        return self.o_isSafe


#######################################################     SLUT PÅ KLASS    ###################################################################################################################
#######################################################     BÖRJAN PÅ TEST   ###################################################################################################################

#url1 = 'github.com'
#u_obj = URL_Object()
#u_obj.setURL(url1)

#print(u_obj.getURL())
#print(u_obj.o_URL)

#u_obj.setURLLength()
#u_obj.setURLFavIcon()
#u_obj.setIP()
#u_obj.setURLSecureProtocol()
#u_obj.setURLSiteAge()

#print('The sites URL is too short(1), too long(2) or ok(0)? ', u_obj.getURLLength())
#print('The site has a favicon ', u_obj.getURLFavIcon())
#print('The sites IP Address: ', u_obj.getIP())
#print('The site has secure protocols: ',u_obj.getURLSecureProtocol())
#print('The Site is too young: ',u_obj.getURLSiteAge())
#print('The site is safe',u_obj.isSafe()) 

#exit