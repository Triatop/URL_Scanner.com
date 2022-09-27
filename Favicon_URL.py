class Favicon_URL(object):
    def getData(self):
        pass
    def hasFavicon(self):
        f_Favicon = False
        if self.getData():
            f_Favicon = True
        return f_Favicon