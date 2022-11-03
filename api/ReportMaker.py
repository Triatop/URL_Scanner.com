from URL_Object import URL_Object

class ReportMaker:
    def __init__(self):
        self.r_URLO = URL_Object()
    def getData(self, u_Obj):
        self.r_URLO = u_Obj
        return 1

    def makeDict(self):
        a_dict = {
            1 : self.r_URLO.getURLFavIcon(),            #1 = Fav Icon 
            2 : self.r_URLO.getURLSecureProtocol(),     #2 = Security protocol
            3 : 0, #need a getter for the protocol here #3 = Port check
            4 : self.r_URLO.getURLSiteAge(),            #4 = Site Age
            5 : self.r_URLO.getURLLength()              #5 = Length
            }
        return a_dict

    def reportMaker(self, a_dict):
        r_str = ""
        for i in range(1,len(a_dict)+1):
            if i == 1:
                r_str += (f"- Website has {'a' if a_dict[i] == 0 else 'no'} favicon ")
            if i == 2:
                r_str += (f"\n- Website uses {'HTTPS'if a_dict[i] == 0 else 'HTTP'} protocol")
            # if i == 3:
            #     r_str += (f"\n- Website is running on the {'right' if a_dict[i] == True else 'wrong'}  port")
            if i == 4:
                case1 = 'is alarmingly young'
                case2 = 'has been running for a credible amount of time'
                r_str += (f"\n- The webiste {case1 if a_dict[i] == 1 else case2}")
            if i == 5:
                case1 = 'of an acceptable length'
                case2 = 'on the border of beeing too long'
                case3 = 'alarmingly long'
                r_str += (f"\n- The url-length is {case1 if a_dict[i] == 0 else case2 if a_dict[i] == 1 else case3 }")
        return r_str