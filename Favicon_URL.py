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
        f_Favicon = False
        if self.getData(f_icon):
            f_Favicon = True
        return f_Favicon
