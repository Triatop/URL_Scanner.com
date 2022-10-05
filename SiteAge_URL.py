import datetime

class SiteAge_URL():
    s_AgeLimit = 100

    def getData(self, s_age):
        try:
            c_dat = s_age['creation_date']
            return c_dat
        except:#<-- If creation_date does not exist
            return False
    def isInLimit(self,s_age):
        isOk = True
        now = datetime.datetime.now()
        if (self.getData(s_age)):
            age = self.getData(s_age)
        else:
            return False
        year = int(now.strftime('%Y')) - int(age.strftime('%Y'))
        month = int(now.strftime('%m')) - int(age.strftime('%m'))
        day = int(now.strftime('%d')) - int(age.strftime('%d'))
        tot = (year * 365) + (month * 30) + day
        if tot > self.s_AgeLimit:
            isOk = False
        return isOk


