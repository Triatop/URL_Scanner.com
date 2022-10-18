from URL_Object import URL_Object
from webscraper import Webscraper
from UrlController import UrlController
from URLLength import LengthURL
from Favicon_URL import Favicon_URL
from SiteAge_URL import SiteAge_URL
from Protocol_URL import Protocol_URL
from SafeEvaluator import SafeEvaluator
from ReportMaker import ReportMaker



url1 = 'https://www.garykessler.net/library/file_sigs.html' #<--- Replace with input
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
r_mkr = ReportMaker()

#Set Values
u_obj.setURL(url1)
w_scrap.setURL(url1)


u_len.getData(url1) #URL Size check
u_prot.getData(w_scrap.exfiltrateProtocol()) #GETTING PROTOCOLS
#HERE ARE THE FINAL VALUES
print(u_obj.getURL())                                            #Get the URL
u_obj.setURLLength(u_len.isURLLong())                            #Is it too long
u_obj.setURLFavIcon(u_fav.hasFavicon(w_scrap.extractFavicon()))  #URL Fav Icon check
u_obj.setURLSecureProtocol(u_prot.isSecure())                    #Security check
u_obj.setIP(u_ctrl.getIP(url1))                                  #Try Set IP We don't use it for anything though
u_obj.setURLSiteAge(u_age.isInLimit(w_scrap.exfiltrateSiteAge()))#How old is site? 

u_obj.isSafe(u_safe.isSafe(u_obj.getURLLength(),u_obj.getURLFavIcon(),u_obj.getURLSecureProtocol(),u_obj.getURLSiteAge())) #UGLY DIRTY SOLUTION that works

r_mkr.getData(u_obj)                                #send URL Object to report maker
o_dic = r_mkr.makeReport()                          #Make the report and catch the output dictionary


print('The sites URL is too long? ', o_dic['1'])    #u_obj.getURLLength())
print('The site has a favicon ', o_dic['2'])        #u_obj.getURLFavIcon())
print('The sites IP Address: ', u_obj.getIP())      #IP
print('The site has secure protocols: ', o_dic['3'])#u_obj.getURLSecureProtocol())
print('The Site is too young: ', o_dic['4'])        #u_obj.getURLSiteAge())
print('The site is safe', o_dic['5'])               #u_obj.getSafe()) 
