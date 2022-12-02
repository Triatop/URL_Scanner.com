from URL_Object import URL_Object

class ReportMaker:
    def __init__(self):
        self.r_str = ""

    def createReport(self, a_dict, siteAge, nrOfMalLinks):
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

        return 

    def getReport(self):
        return self.r_str
