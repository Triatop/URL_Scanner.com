import datetime

class SiteAge_URL():
    s_AgeLimit = 100 #REPLACE WITH AN ACTUAL LIMIT

    def getData(self, s_age):
        try:
            c_dat = s_age["creation_date"]
            return c_dat
        except:#<-- If creation_date does not exist
            return False
    def isInLimit(self,s_age):
        isOk = True
        now = datetime.datetime.now()
        if (self.getData(s_age)):
            age = self.getData(s_age)
        else:
            return
        year = int(now.strftime('%Y')) - int(age.strftime('%Y'))
        month = int(now.strftime('%m')) - int(age.strftime('%m'))
        day = int(now.strftime('%d')) - int(age.strftime('%d'))
        tot = (year * 365) + (month * 30) + day #Month is on average 30 days
        if tot > self.s_AgeLimit:
            isOk = False
        return isOk

    def isExpired(self, s_dat):
        isExp = False
        e_dat = s_dat["expiration_date"]
        now = datetime.datetime.now()
        year =  int(e_dat.strftime('%Y')) - int(now.strftime('%Y'))
        month = int(e_dat.strftime('%m')) - int(now.strftime('%m'))
        day = int(e_dat.strftime('%d')) - int(now.strftime('%d'))
        expire = (year * 365) + (month * 30) + day #Month is on average 30 days
        if expire < 0:
            isExp = True
        return isExp

    def currAge(self, s_age): #Site age in days
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

