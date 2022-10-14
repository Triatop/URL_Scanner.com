from URL_Object import URL_Object
from webscraper import Webscraper
from UrlController import UrlController
from URLLength import LengthURL
from Favicon_URL import Favicon_URL
from SiteAge_URL import SiteAge_URL
from Protocol_URL import Protocol_URL
from SafeEvaluator import SafeEvaluator
from htmldate import find_date



url1 = 'https://www.garykessler.net/library/file_sigs.html' #<--- Replace with input
#url1 = 'Victor was here :) \n\t lllllllllllllll' #<--- not a real url for testing purposes
u_ctrl = UrlController()

print(u_ctrl.splitUrl(url1))
if (u_ctrl.validateUrl(url1)  != True) : #<--- if website fails to validate
    raise SystemExit#<--- Return to sender

#Classes
u_obj = URL_Object()
w_scrap = Webscraper()
u_len = LengthURL()
u_fav = Favicon_URL()
u_age = SiteAge_URL()
u_prot = Protocol_URL()
u_safe = SafeEvaluator()


#Variables For Testing

#f_ic = []
#d_lin = []
#d_dat = {}
#s_pro = ''
#o_len = 0

#Set Values
u_obj.setURL(url1)
w_scrap.setURL(url1)

#Get Values Testing!
#print(w_scrap.getURL())
#f_ic = w_scrap.extractFavicon()
#d_lin = w_scrap.findLinks()
#d_dat = w_scrap.exfiltrateSiteAge()
#s_pro = w_scrap.exfiltrateProtocol()
#print('Fav icon ', f_ic, '\nLinks ', len(d_lin), '\nDates ', d_dat, '\nSec protocols ',s_pro)
#print(u_obj.o_URL)

u_len.getData(url1) #URL Size check
u_prot.getData(w_scrap.exfiltrateProtocol()) #GETTING PROTOCOLS
#print(u_prot.secureProtocols, u_prot.currentProtocol) #test
#HERE ARE THE FINAL VALUES
print(u_obj.getURL())
u_obj.setURLLength(u_len.isURLLong())                                       #Is it too long
u_obj.setURLFavIcon(u_fav.hasFavicon(w_scrap.extractFavicon())) #URL Fav Icon check
u_obj.setURLSecureProtocol(u_prot.isSecure())                   #Security check
u_obj.setIP(u_ctrl.getIP(url1))                                 #Try Set IP We don't use it for anything though
u_obj.setURLSiteAge(u_age.isInLimit(w_scrap.exfiltrateSiteAge())) 
#print(find_date('https://www.garykessler.net/library/file_sigs.html'))
u_obj.isSafe(u_safe.isSafe(u_obj.getURLLength(),u_obj.getURLFavIcon(),u_obj.getURLSecureProtocol(),u_obj.getURLSiteAge())) #UGLY DIRTY SOLUTION




#TO BE REPLACED WITH REPORTMANAGER THING!!!!
print('The sites URL is too long(1) or ok(0)? ', u_obj.getURLLength())
print('The site has a favicon ', u_obj.getURLFavIcon())
print('The sites IP Address: ', u_obj.getIP())
print('The site has secure protocols: ',u_obj.getURLSecureProtocol())
print('The Site is too young: ',u_obj.getURLSiteAge())
print('The site is safe',u_obj.getSafe()) 
