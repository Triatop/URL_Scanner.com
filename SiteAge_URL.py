import datetime

class SiteAge_URL():
    s_AgeLimit = 100 #REPLACE WITH AN ACTUAL LIMIT

    def getData(self, s_age):
        pass
    def isInLimit(self,s_age):
        isOk = True
        now = datetime.date.now()
        age = s_age
        year = int(now.strftime('%Y')) - int(age.strftime('%Y'))
        month = int(now.strftime('%m')) - int(age.strftime('%m'))
        day = int(now.strftime('%d')) - int(age.strftime('%d'))
        tot = (year * 365) + (month * 30) + day #Month is on average 30 days
        if tot > self.s_AgeLimit:
            isOk = False
        return isOk

    def currAge(self, s_age): #Site age in days not in use
        now = datetime.datetime.now()
        if (self.getData(s_age)):
            age = self.getData(s_age)
        else:
            return
        year = int(now.strftime('%Y')) - int(age.strftime('%Y'))
        month = int(now.strftime('%m')) - int(age.strftime('%m'))
        day = int(now.strftime('%d')) - int(age.strftime('%d'))
        t_age = (year * 365) + (month * 30) + day #Month is on average 30 days
        return t_age

