from requests_html import HTMLSession
import re

class Webscraper:
    def __init__(self, url = ""):
        self.url = url if url else ""
        self.r = ""
        self.session = HTMLSession()
        return
    def setURL(self, url):
        self.url = url
        return 1
    def getURL(self):
        #Primarily used for testing
        return self.url
    def isExistFavicon(self):
        #Might need to speed this up for when favicon is not found
        self.r = self.session.get(self.url).text
        pattern = ".*rel=\"[shortcut icon|icon].*\""
        return 1 if re.search(pattern, self.r) else 0
