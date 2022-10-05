from URL_Object import URL_Object
from webscraper import Webscraper
from UrlController import UrlController
from URLLength import LengthURL
from Favicon_URL import Favicon_URL
from SiteAge_URL import SiteAge_URL
from Protocol_URL import Protocol_URL
import sys
#TODO
#Class Safe Evaluator
#Class Sec_prot
#Test webscraper
#FIX ATTRIBUTE CLASSES

#url controller check.

url1 = 'https://www.google.com/' #<--- Replace with input
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


#Variables

f_ic = []
d_lin = []
d_dat = {}
s_pro = ''
o_len = 0


u_obj.setURL(url1)
w_scrap.setURL(url1)

print(w_scrap.getURL())

f_ic = w_scrap.extractFavicon()
d_lin = w_scrap.findLinks()
try:
    d_dat = w_scrap.exfiltrateSiteAge()
except:
    pass
s_pro = w_scrap.exfiltrateProtocol()

print('Fav icon ', f_ic, '\nLinks ', len(d_lin), '\nDates ', d_dat, '\nSec protocols ',s_pro)


print(u_obj.getURL())
#print(u_obj.o_URL)
u_len.getData(url1) #URL Size check
if(u_len.isURLLong()):
     o_len = u_len.isURLLong()
else:
     o_len = u_len.isURLShort()
u_obj.setURLLength(o_len)
u_obj.setURLFavIcon(u_fav.hasFavicon(f_ic)) #URL Fav Icon check
u_obj.setIP(u_ctrl.getIP(url1))
u_obj.setURLSiteAge(u_age.isInLimit(d_dat))

print('The sites URL is too short(1), too long(2) or ok(0)? ', u_obj.getURLLength())
print('The site has a favicon ', u_obj.getURLFavIcon())
print('The sites IP Address: ', u_obj.getIP())
print('The site has secure protocols: ',u_obj.getURLSecureProtocol())
print('The Site is too young: ',u_obj.getURLSiteAge())
print('The site is safe',u_obj.isSafe()) 

