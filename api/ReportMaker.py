from URL_Object import URL_Object

class ReportMaker:
    def __init__(self):
        self.r_str = ""

    def createReport(self, a_dict, siteAge):
        self.r_str = ""
        
        #Fav Icon
        self.r_str += (f"- Website has {'a' if a_dict[1] == 0 else 'no'} favicon ")
            
        #Secutiry Protocol
        self.r_str += (f"\n- Website uses {'HTTPS'if a_dict[2] == 0 else 'HTTP'} protocol")
        
        #Port
        self.r_str += (f"\n- Website is running on the {'right' if a_dict[3] == 0 else 'wrong'} port")
            
        #Site Age 
        case1 = 'is alarmingly young'
        case2 = 'has been running for a credible amount of time'
        self.r_str += (f"\n- The webiste {case1 if a_dict[4] == 1 else case2} ({siteAge} days)")
        
        #Length
        case1 = 'of an acceptable length'
        case2 = 'on the border of beeing too long'
        case3 = 'alarmingly long'
        self.r_str += (f"\n- The url-length is {case1 if a_dict[5] == 0 else case2 if a_dict[5] == 1 else case3 }")

        return 

    def getReport(self):
        return self.r_str
