import sys
import urllib.request as urllib2

class CertValidator:
    def __init__(self, url = ""):
        self.url = url
    def validateCert(self, url = ""):
        req = urllib2.Request(url if url != "" else self.url)
        try:
            urllib2.urlopen(req)
        except urllib2.URLError as err:
            return err
        return 0
    def processData(self, url = ""):
        return 1 if self.validateCert(url if url != "" else self.url) else 0
