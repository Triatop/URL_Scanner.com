class Favicon_URL(object):
    def getData(self, f_icon):
        try:
            if(len(f_icon) > 0):
                return True
            else:
                return False
        except:
            return False
    def hasFavicon(self, f_icon):
        f_Favicon = 0
        if self.getData(f_icon):
            f_Favicon = 1
        return f_Favicon