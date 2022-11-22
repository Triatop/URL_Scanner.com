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
from SpecialCharactersCheck import SpecialCharactersCheck
from certValidator import CertValidator
from PortCheck import PortCheck


def main(url1, report=True):
    u_ctrl = UrlController()
    url1 = u_ctrl.addProtocol(url1)
    
    #Redirect check
    urlRedirect = u_ctrl.checkRedirect(url1)
    if url1 != urlRedirect:
        url1 = urlRedirect
        urlRedirect = True
    else:
        urlRedirect = False

    ip = u_ctrl.validateUrl(url1)
    

    #Check if wevsite is valid (exists) - else early return
    if not ip: #<--- if website fails to validate
        return {"valid": "False", "report": "- Invalid URL, website does not exist - check for spelling errors"}

    #Attribute Classes
    u_obj = URL_Object() 
    u_fav = Favicon_URL()
    u_prot = Protocol_URL()
    u_mlin = MaliciousLinks()
    u_scc = SpecialCharactersCheck()
    u_cert = CertValidator()
    u_len = LengthURL()
    u_age = SiteAge_URL() 
    u_port = PortCheck()

    #Funciton Classes
    w_scrap = Webscraper()
    r_mkr = ReportMaker()
    u_safe = SafeEvaluator()

    #Set Values
    u_obj.setURL(url1)
    u_scc.setData(url1)
    w_scrap.setURL(url1)
    u_mlin.getData(url1, w_scrap.findLinks())
    u_obj.setIP(ip)                                     #Try Set IP We don't use it for anything though


    u_len.getData(url1) #URL Size check
    u_prot.getData(w_scrap.exfiltrateProtocol()) #GETTING PROTOCOLS

    #HERE ARE THE FINAL VALUES
    u_obj.setURLLength(u_len.isURLLong())                               #Is it too long
    u_obj.setURLFavIcon(u_fav.hasFavicon(w_scrap.extractFavicon()))     #URL Fav Icon check
    u_obj.setURLSecureProtocol(u_prot.isSecure())                       #Security check
    u_obj.setCheckPort(u_port.checkPorts(u_obj.getIP(), w_scrap.exfiltrateProtocol()))                    #Is the site runnig on the right port?
    u_obj.setURLLength(u_len.isURLLong())                               #Is it too long
    u_obj.setURLSiteAge(u_age.isInLimit(w_scrap.exfiltrateSiteAge()))   #How old is site? 
    u_obj.setSpecialCharater(u_scc.processData())                       #Looking for special charactes
    u_obj.setCertificateValid(u_cert.processData(url1))                 #Certificate validation
    u_obj.setURLLinks(u_mlin.isExternalSafe())                          #Are the external links malicious/How malicious are they?

    #Make the attribute dictionary and create report
    u_obj.makeDict()                                    
    r_mkr.createReport(u_obj.getDict(), w_scrap.exfiltrateSiteAge().days, u_mlin.getNrOfMalLinks())
    u_obj.setSafe(u_safe.isSafe(u_obj.getDict()))                 #Safe eveluator check

    print(u_obj.getDict())

    if(report):
        return {"valid": "True","report": r_mkr.getReport(), "binarySafe": u_obj.getSafe(), "reDirect": f"\n\nRedirected: {urlRedirect} \nScanning: {url1}"}
    else:
        return u_obj.getDict()
