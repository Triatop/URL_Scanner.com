import datetime

class SiteAge_URL():
    def __init__(self):
        self.s_AgeLimit = 180 #6 MONTHS DECLARED AS PHISHING

    def getData(self):
        a_limit = datetime.timedelta(days = self.s_AgeLimit)
        return a_limit
    def isInLimit(self,s_age):
        isNotOk = 1
        tot = s_age
        a_limit = self.getData()
        #year = int(now.strftime('%Y')) - int(age.strftime('%Y'))
        #month = int(now.strftime('%m')) - int(age.strftime('%m'))
        #day = int(now.strftime('%d')) - int(age.strftime('%d'))
        #tot = (year * 365) + (month * 30) + day #Month is on average 30 days
        if tot > a_limit:
            isNotOk = 0
        return isNotOk

