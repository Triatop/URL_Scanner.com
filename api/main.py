from URL_Object import URL_Object
from webscraper import Webscraper
from UrlController import UrlController
from URLLength import LengthURL
from MaliciousLinks import MaliciousLinks
from Favicon_URL import Favicon_URL
from SiteAge_URL import SiteAge_URL
from Protocol_URL import Protocol_URL
from SafeEvaluator import SafeEvaluator
from ReportMaker import ReportMaker


def main(url1, report=True):
    u_ctrl = UrlController()
    url1 = u_ctrl.addProtocol(url1)
    
    if not u_ctrl.validateUrl(url1): #<--- if website fails to validate
        return {"valid": "False", "report": "- Invalid URL, website does not exist - check for spelling errors"}
    url1 = u_ctrl.checkRedirect(url1)
    #Classes
    u_obj = URL_Object()
    w_scrap = Webscraper()
    u_len = LengthURL()
    u_fav = Favicon_URL()
    u_age = SiteAge_URL()
    u_prot = Protocol_URL()
    u_mlin = MaliciousLinks()
    u_safe = SafeEvaluator()
    r_mkr = ReportMaker()

    #Set Values
    u_obj.setURL(url1)
    w_scrap.setURL(url1)
    u_mlin.getData(url1, w_scrap.findLinks())

    print(w_scrap.url)



    u_len.getData(url1) #URL Size check
    u_prot.getData(w_scrap.exfiltrateProtocol()) #GETTING PROTOCOLS

    #HERE ARE THE FINAL VALUES
    u_obj.setURLLength(u_len.isURLLong())                               #Is it too long
    u_obj.setURLLinks(u_mlin.maliciousCheck())                          #Are the external links malicious/How malicious are they?
    u_obj.setURLFavIcon(u_fav.hasFavicon(w_scrap.extractFavicon()))     #URL Fav Icon check
    u_obj.setURLSecureProtocol(u_prot.isSecure())                       #Security check
    u_obj.setIP(u_ctrl.getIP(url1))                                     #Try Set IP We don't use it for anything though
    u_obj.setURLSiteAge(u_age.isInLimit(w_scrap.exfiltrateSiteAge()))   #How old is site? 
    u_obj.setCheckPort(w_scrap.exfiltrateProtocol())

    u_obj.makeDict()                                    #Make the attribute dictionary
    r_mkr.createReport(u_obj.getDict(), w_scrap.exfiltrateSiteAge().days) #Create report from attribute dict and site age 

    u_obj.setSafe(u_safe.isSafe(u_obj.getDict()))                 #Safe eveluator check

    if(report):
        return {"valid": "True","report": r_mkr.getReport(), "binarySafe": f" Website is {'SAFE' if u_obj.getSafe() else 'NOT SAFE'} to enter"}
    else:
        return u_obj.getDict()
