import datetime

class SiteAge_URL():
    s_AgeLimit = 100

    def getData(self):
        return datetime.datetime(2020, 5, 17) #<-- Replace with actual age of site

    def isInLimit(self):
        isOk = True
        now = datetime.datetime.now()
        age = self.getData()
        year = int(now.strftime('%Y')) - int(age.strftime('%Y'))
        month = int(now.strftime('%m')) - int(age.strftime('%m'))
        day = int(now.strftime('%d')) - int(age.strftime('%d'))
        tot = (year * 365) + (month * 30) + day
        if tot > self.s_AgeLimit:
            isOk = False
        return isOk


