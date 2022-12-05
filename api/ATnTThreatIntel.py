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
        if self.__checkValidInput(url, method = ".maliciousFiles()"):
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
    def getMaliciousFilesCount(self, url = "", limit = 100):
        """
        """
        url = self.url if url == "" else url
        if self.__checkValidInput(url, method = ".getMaliciousFilesCount()"):
            return None
        passive_dns = requests.get(f"https://otx.alienvault.com/api/v1/indicators/hostname/{url}/passive_dns").json()["passive_dns"]
        addresses = []
        filesCount = requests.get("https://otx.alienvault.com/api/v1/indicators/hostname/{}/malware".format(url)).json()["count"]
        for add in passive_dns:
            addresses.append(add["address"])
        for add in addresses:
            try:
                if re.match("[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", add):
                    filesCount += requests.get("https://otx.alienvault.com/api/v1/indicators/IPv4/{}/malware".format(add)).json()["count"]
                else:
                    filesCount += requests.get("https://otx.alienvault.com/api/v1/indicators/hostname/{}/malware".format(add)).json()["count"]
                if(filesCount > limit-1):
                    filesCount = limit
                    break
            except KeyError:
                continue
        return filesCount


    def getGeoLocation(self, url = ""):
        """
            Grabs the geo location from otx.alienvault.com
            Returns Geolocation
        """
        url = self.url if url == "" else url
        if self.__checkValidInput(url, method = ".getGeoLocation()"):
            return None
        return requests.get(f"https://otx.alienvault.com/api/v1/indicators/domain/{url}/geo").json()["flag_title"]

    def pulseCount(self, url = ""):
        """
            Checks otx.alienvault.com threat intel for known pulses
            Returns amount of pulses the domain is included in.
        """
        url = self.url if url == "" else url
        if self.__checkValidInput(url, method=".pulseCount()"):
            return None
        url = self.__getDomain(url)
        req = requests.get(f"https://otx.alienvault.com/api/v1/indicators/domain/{url}/general").json()
        return req["pulse_info"]["count"]
        

    def __checkValidInput(self, url, method):
        """
            Internal method, do not use outside of this class
        """
        if not len(url):
            logging.warning(f"Invalid URL \"{url}\" was given to ATnTThreatIntel{method}")
            return 1
        return 0

    def __getDomain(self, url):
        url = re.split("w{3}\.", url)[1]
        url = re.split("/", url)[0]
        while(len(re.findall("\.", url)) > 1):
            url = re.findall("\..*\.com$", url)[0][1:]
        return url
