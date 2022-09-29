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
            favIcons.append(f.get('href'))
        for f in soup.findAll(rel="shortcut icon"):
            favIcons.append(f.get('href'))
        return favIcons
    def isExistFavicon(self):
        #Might need to speed this up for when favicon is not found
        self.r = self.session.get(self.url).text
        pattern = re.compile(".*rel=\"(shortcut icon|icon).*ico.*")
        return 1 if re.search(pattern, self.r) else 0
    def findLinks(self):
        links = []
        self.r = self.session.get(self.url).text
        soup = BeautifulSoup(self.r, "lxml")
        for link in soup.findAll('a'):
            links.append(link.get('href'))

        return links
    def exfiltrateSiteAge(self):
        domain = whois.query(re.search("www\..*", self.url)[0])
        return {"creation_date": domain.creation_date, "expiration_date" : domain.expiration_date}
    def exfiltrateProtocol(self):
        # Needs to have url set to <protcol>://<url> to fully work
        protocol = self.url.split(':')[0]
        self.r = self.session.get(self.url)
        try:
            if self.r.history[0].status_code == 301:
                protocol = self.r.url.split(':')[0]
        except IndexError:
            1 == 1
        return protocol

if __name__ == "__main__":
    ws = Webscraper("http://www.w3schools.com/python/python_datetime.asp")
    print(ws.exfiltrateProtocol())
