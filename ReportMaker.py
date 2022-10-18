from URL_Object import URL_Object

class ReportMaker:
    def __init__(self):
        self.r_URLO = URL_Object()
    def getData(self, u_Obj):
        self.r_URLO = u_Obj
        return 1

    def makeReport(self):
        r_dict = {
            '1' : self.r_URLO.getURLLength(),           #1 = Length 
            '2' : self.r_URLO.getURLFavIcon(),          #2 = Fav Icon
            '3' : self.r_URLO.getURLSecureProtocol(),   #3 = Security protocol
            '4' : self.r_URLO.getURLSiteAge(),          #4 = Site age
            '5' : self.r_URLO.getSafe()                 #5 = Is Safe
            }
        return r_dict