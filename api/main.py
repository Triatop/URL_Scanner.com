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
from DB_Controller import DBController
from CharSwap import CharSwap
from ATnTThreatIntel import ATnTThreatIntel

import logging

def main(url1, username, report=True):
    FORMAT = f'%(asctime)s-%(levelname)s-{username}-%(message)s'
    logging.basicConfig(filename="urlscan.log", filemode='a',format=FORMAT, level=logging.INFO, )
    logging.info(f"Starting: Scan on {url1}")
    u_ctrl = UrlController()
    url1 = u_ctrl.addProtocol(url1)
    original_url = url1
    
    logging.info(f"Starting: Redirect")
    #Redirect check
    urlRedirect = u_ctrl.checkRedirect(url1)
    if url1 != urlRedirect:
        url1 = urlRedirect
        urlRedirect = True
    else:
        urlRedirect = False

#-------------------- DELETE THIS CODE MAYBE ---------------------

    # ~~~ Check if scan exists in DB alread ~~~

    # db_obj = DBController()
    # parms = None
    # for scan in db_obj.getPrevScans():
    #     if (url1 == scan['url']):
    #         parms = scan
    #         break
    #     continue
    # if(parms != None):
    #     r_mkr = ReportMaker()
    #     attr_dict = {int(k):v for k,v in parms['attributes'].items()} 
    #     r_mkr.createReport(attr_dict, parms['site_age'],parms['mal_links'],parms['char_swap_url'])
    #     db_obj.insertScan(username, u_ctrl.encryptUrl(parms['url']), parms['s_value'], attr_dict, parms['site_age'],parms['mal_links'],parms['char_swap_url'])
    #     return {"valid": True,"report": (f"\n\n{r_mkr.getReport()}"), "binarySafe": parms['s_value'], "reDirect": f"Redirected: {urlRedirect} \nScanning: {url1}"}

#-----------------------------------------------------------------

    logging.info(f"Starting: Validate")
    #Check if wevsite is valid (exists) - else early return
    if not u_ctrl.validateUrl(url1): #<--- if website fails to validate
        return {"valid": False, "report": "- Invalid URL, website does not exist, check for spelling errors"}

    #Attribute Classes
    logging.info(f"Starting: Creating attribute objects")
    u_obj = URL_Object() 
    u_fav = Favicon_URL()
    u_prot = Protocol_URL()
    u_mlin = MaliciousLinks()
    u_scc = SpecialCharactersCheck()
    u_cert = CertValidator()
    u_len = LengthURL()
    u_age = SiteAge_URL() 
    u_port = PortCheck()
    u_cswp = CharSwap()
    u_tint = ATnTThreatIntel()
    logging.info(f"Done: Creating attribute objects")

    #Function Classes
    logging.info(f"Starting: Creating function objects")
    w_scrap = Webscraper()
    r_mkr = ReportMaker()
    u_safe = SafeEvaluator()
    logging.info(f"Done: Creating function objects")

    #Set Values
    logging.info(f"Starting: Set initial object values")
    u_obj.setURL(url1)
    u_scc.setData(url1)
    print(original_url)
    u_cswp.getData(original_url)
    w_scrap.setURL(url1)
    u_mlin.getData(url1, w_scrap.findLinks())
    u_obj.setIP(u_ctrl.getIP(url1))                                     #Try Set IP We don't use it for anything though
    logging.info(f"Done: Set initial object values")

    u_len.getData(url1) #URL Size check
    u_prot.getData(w_scrap.exfiltrateProtocol()) #GETTING PROTOCOLS

    #HERE ARE THE FINAL VALUES
    logging.info(f"Starting: Get features")
    logging.info(f"Fetching: URL Length")                                           
    u_obj.setURLLength(u_len.isURLLong())                                               #Is it too long
    logging.info(f"Fetching: Favicon")
    u_obj.setURLFavIcon(u_fav.hasFavicon(w_scrap.extractFavicon()))                     #URL Fav Icon check
    logging.info(f"Fetching: Protocol")
    u_obj.setURLSecureProtocol(u_prot.isSecure())                                       #Security check
    logging.info(f"Fetching: Port Check")
    u_obj.setCheckPort(u_port.checkPorts(u_obj.getIP(), w_scrap.exfiltrateProtocol()))  #Is the site runnig on the right port?
    logging.info(f"Fetching: URL Length")
    u_obj.setURLLength(u_len.isURLLong())                                               #Is it too long
    logging.info(f"Fetching: Age Limit")
    u_obj.setURLSiteAge(u_age.isInLimit(w_scrap.exfiltrateSiteAge()))                   #How old is site? 
    logging.info(f"Fetching: Special Character")
    u_obj.setSpecialCharater(u_scc.processData())                                       #Looking for special charactes
    logging.info(f"Fetching: Certificate")
    u_obj.setCertificateValid(u_cert.processData(url1))                                 #Certificate validation
    logging.info(f"Fetching: Malicious Links")
    u_obj.setURLLinks(u_mlin.isExternalSafe())                                          #Are the external links malicious/How malicious are they?
    logging.info(f"Fetching: Character Swap")
    u_obj.setIsCharSwapped(u_cswp.isCharSwap())                                         #is it mimicing a website by swapping a char in the name to one that is similar
    logging.info(f"Fetching: Pulse Count")
    u_obj.setPulseCount(u_tint.pulseCount(url1))                                        #How many pulses has it been included in?
    logging.info(f"Fetching: Malicious Files")
    u_obj.setMalFileCount(u_tint.getMaliciousFilesCount(url1))                          #How many malicious files are associated with it
    logging.info(f"Done: Get features")


    #Make the attribute dictionary and create report
    logging.info(f"Starting: Report creation")
    u_obj.makeDict()                                    
    r_mkr.createReport(u_obj.getDict(), w_scrap.exfiltrateSiteAge().days, u_mlin.getNrOfMalLinks(),u_cswp.getsus_url() )
    u_obj.setSafe(u_safe.isSafe(u_obj.getDict()))                 #Safe eveluator check
    logging.info(f"Done: Report creation")
    logging.info(f"Done: scan on {url1}")
    if(report):
        logging.info(f"Starting: Inserting scan in Data Base")
        db_obj = DBController()
        db_obj.insertScan(username, u_ctrl.encryptUrl(url1), u_obj.getSafe(), u_obj.getDict(), w_scrap.exfiltrateSiteAge().days, u_mlin.getNrOfMalLinks(), u_cswp.getsus_url())
        logging.info(f"Done: Inserting scan in Data Base")
        return {"valid": True,"report": (f"\n\n{r_mkr.getReport()}"), "binarySafe": u_obj.getSafe(), "reDirect": f"Redirected: {urlRedirect} \nScanning: {url1}"}
    else:
        return u_obj.getDict()

