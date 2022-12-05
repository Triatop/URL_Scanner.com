from URL_Object import URL_Object

class ReportMaker:
    def __init__(self):
        self.r_str = ""

    def createReport(self, a_dict, siteAge, nrOfMalLinks, charSwapURL):
        self.r_str = ""
        
        #Fav Icon
        self.r_str += (f"· Website has {'a' if a_dict[1] == 0 else 'no'} favicon ")
            
        #Secutiry Protocol
        self.r_str += (f"\n· Website uses {'HTTPS'if a_dict[2] == 0 else 'HTTP'} protocol")
        
        #Port
        self.r_str += (f"\n· Website is running on the {'right' if a_dict[3] == 0 else 'wrong'} port")
            
        #Site Age 
        case1 = 'is not very old'
        case2 = 'has existed for a long time'
        self.r_str += (f"\n· The website {case1 if a_dict[4] == 1 else case2} - {siteAge} days")
        
        #Length
        case1 = 'acceptable'
        case2 = 'on the border of beeing too long'
        case3 = 'alarmingly long'
        self.r_str += (f"\n· The url-length is {case1 if a_dict[5] == 0 else case2 if a_dict[5] == 1 else case3 }")

        #Specail Character
        case1 = 'no special characters'
        case2 = 'special characters'
        self.r_str += (f"\n· The url contains {case1 if a_dict[6] == 0 else case2}")

        #Certificate Validation
        self.r_str += (f"\n· Certificate is {'valid' if a_dict[7] == 0 else 'invalid'}")

        #Malisouls links
        self.r_str += (f"\n· Number of malicious external links: {nrOfMalLinks}")

        #Character Swap
        case1 = "has no letters that seem to be swapped"
        case2 = "has accented characters but it does not appear to mimic any of the most popular websites"
        case3 = "Is likely attempting to mimic " + charSwapURL
        self.r_str += (f"\n· The domain name  {case3 if a_dict[9] == 1 else case2 if charSwapURL != '' else case1} ")

        #Pulse count
        self.r_str += (f"\n· Number of pulses: {a_dict[10]}")

        #Malicious File count
        self.r_str += (f"\n· Number of malicious files associated with this url: {a_dict[11]}")

        return 

    def getReport(self):
        return self.r_str
