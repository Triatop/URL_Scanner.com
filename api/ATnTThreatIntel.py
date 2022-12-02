import requests
import re
import logging


class ATnTThreatIntel:
    def __init__(self, url = ""):
        self.url = url
    def maliciousFiles(self, url = ""):
        """
            Finds all IP addresses related to a url/domain and looks for malicious files hosted on that IP.
            Returns Dictionary with {IP:<files count>}
        """
        url = self.url if url == "" else url
        if self.checkValidInput(url, method = ".maliciousFiles()") == 0:
            return None
        passive_dns = requests.get(f"https://otx.alienvault.com/api/v1/indicators/hostname/{url}/passive_dns").json()["passive_dns"]
        addresses = []
        filesCount = {}
        filesCount[url] = requests.get("https://otx.alienvault.com/api/v1/indicators/hostname/{}/malware".format(url)).json()["count"]
        for add in passive_dns:
            addresses.append(add["address"])
        for add in addresses:
            try:
                if re.match("[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", add):
                    filesCount[add] = requests.get("https://otx.alienvault.com/api/v1/indicators/IPv4/{}/malware".format(add)).json()["count"]
                else:
                    filesCount[add] = requests.get("https://otx.alienvault.com/api/v1/indicators/hostname/{}/malware".format(add)).json()["count"]
            except KeyError:
                continue
        return filesCount

    def getGeoLocation(self, url = ""):
        """
            Grabs the geo location from otx.alienvault.com
            Returns Geolocation
        """
        url = self.url if url == "" else url
        if self.checkValidInput(url, method = ".getGeoLocation()") == 0:
            return None
        return requests.get(f"https://otx.alienvault.com/api/v1/indicators/domain/{url}/geo").json()["flag_title"]

    def pulseCount(self, url = ""):
        """
            Checks otx.alienvault.com threat intel for known pulses
            Returns amount of pulses the domain/url is included in.
        """
        url = self.url if url == "" else url
        if self.checkValidInput(url, method=".pulseCount()") == 0:
            return None
        return requests.get(f"https://otx.alienvault.com/api/v1/indicators/domain/{url}/general").json()["pulse_info"]["count"]

    def checkValidInput(self, url, method):
        """
            Internal method, do not use outside of this class
        """
        if not len(url):
            logging.warning(f"Invalid URL \"{url}\" was given to ATnTTheatIntel{method}")
        return 0