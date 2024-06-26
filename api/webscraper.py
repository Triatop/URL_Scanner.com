from datetime import datetime, timedelta
from requests_html import HTMLSession
import re
import whois
from bs4 import BeautifulSoup

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
    def extractFavicon(self):
        favIcons = []
        self.r = self.session.get(self.url).text
        soup = BeautifulSoup(self.r, "lxml")
        for f in soup.findAll(rel="icon"):
            try:
                favIcons.append(f.get('href').split(".ico")[0]+".ico")
            except IndexError:
                1
        for f in soup.findAll(rel="shortcut icon"):
            try:
                favIcons.append(f.get('href').split(".ico")[0]+".ico")
            except IndexError:
                1
        return favIcons
    def isExistFavicon(self):
        return 1 if self.extractFavicon() else 0
    def findLinks(self):
        links = []
        self.r = self.session.get(self.url).text
        soup = BeautifulSoup(self.r, "lxml")
        for link in soup.findAll('a'):
            links.append(link.get('href'))

        return links

    def exfiltrateSiteAge(self):
        try:
            domain = whois.whois(re.search("www\..*", self.url)[0])
        except TypeError:
            domain = whois.whois(self.url)
        if (domain.creation_date == None):
            return timedelta(days = 0)
        try:
            return datetime.now() - domain.creation_date[0]
        except TypeError:
            return datetime.now() - domain.creation_date

    def exfiltrateProtocol(self):
        # Needs to have url set to <protcol>://<url> to fully work
        protocol = self.url.split(':')[0]
        self.r = self.session.get(self.url)
        try:
            if self.r.history[0].status_code == 301:
                protocol = self.r.url.split(':')[0]
        except IndexError:
            1
        return protocol

if __name__ == "__main__":
    1
