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
        url = self.__getDomain(url)
        try:
            passive_dns = requests.get(f"https://otx.alienvault.com/api/v1/indicators/hostname/{url}/passive_dns").json()["passive_dns"]
        except EnvironmentError as err:
            logging.warning(f"ATnTThreatIntel.maliciousFiles({add}) - {err}")
        addresses = []
        filesCount = {}
        try:
            filesCount[url] = requests.get("https://otx.alienvault.com/api/v1/indicators/hostname/{}/malware".format(url)).json()["count"]
        except EnvironmentError as err:
            logging.warning(f"ATnTThreatIntel.maliciousFiles({add}) - {err}")
        for add in passive_dns:
            addresses.append(add["address"])
        for add in addresses:
            try:
                if re.match("^ns|^NXDOMAIN", add):
                    continue
                if re.match(r"(\d{1,3}\.){3}\d{1,3}", add):
                    try:
                        filesCount[add] = requests.get("https://otx.alienvault.com/api/v1/indicators/IPv4/{}/malware".format(add)).json()["count"]
                    except:
                        logging.warning(f"Couldn't process {add} in .getMaliciousFilesCount() /IPv4/../malware api call")
                elif re.match("^((\d|\w){0,4}:){1,7}(\d|\w){0,4}", add):
                    try:
                        filesCount[add] = requests.get("https://otx.alienvault.com/api/v1/indicators/IPv6/{}/malware".format(add)).json()["count"]
                    except:
                        logging.warning(f"Couldn't process {add} in .getMaliciousFilesCount() /IPv6/../malware api call")
                else:
                    try:
                        filesCount[add] = requests.get("https://otx.alienvault.com/api/v1/indicators/hostname/{}/malware".format(add)).json()["count"]
                    except:
                        logging.warning(f"Couldn't process {add} in .getMaliciousFilesCount() /hostname/../malware api call")
            except KeyError:
                continue
            except EnvironmentError as err:
                logging.warning(f"ATnTThreatIntel.maliciousFiles({add}) - {err}")
                continue
        return filesCount
    def getMaliciousFilesCount(self, url = "", limit = 100):
        """
        """
        url = self.url if url == "" else url
        if self.__checkValidInput(url, method = ".getMaliciousFilesCount()"):
            return None
        url = self.__getDomain(url)
        try:
            passive_dns = requests.get(f"https://otx.alienvault.com/api/v1/indicators/hostname/{url}/passive_dns").json()["passive_dns"]
        except EnvironmentError as err:
            logging.warning(f"ATnTThreatIntel.maliciousFilesCount({add}, {limit}) - {err}")
        addresses = []
        try:
            filesCount = requests.get("https://otx.alienvault.com/api/v1/indicators/hostname/{}/malware".format(url)).json()["count"]
        except EnvironmentError as err:
            logging.warning(f"ATnTThreatIntel.maliciousFilesCount({add}, {limit}) - {err}")
        for add in passive_dns:
            addresses.append(add["address"])
        addresses = [*set(addresses)]   # Clear duplicate addresses
        for add in addresses:
            try:
                if re.match("^ns|^NXDOMAIN", add):
                    continue
                if re.match(r"(\d{1,3}\.){3}\d{1,3}", add):
                    try:
                        filesCount += requests.get("https://otx.alienvault.com/api/v1/indicators/IPv4/{}/malware".format(add)).json()["count"]
                    except:
                        logging.warning(f"Couldn't process {add} in .getMaliciousFilesCount() /IPv4/../malware api call")
                elif re.match("^((\d|\w){0,4}:){1,7}(\d|\w){0,4}", add):
                    try:
                        filesCount += requests.get("https://otx.alienvault.com/api/v1/indicators/IPv6/{}/malware".format(add)).json()["count"]
                    except:
                        logging.warning(f"Couldn't process {add} in .getMaliciousFilesCount() /IPv6/../malware api call")
                else:
                    try:
                        filesCount += requests.get("https://otx.alienvault.com/api/v1/indicators/hostname/{}/malware".format(add)).json()["count"]
                    except:
                        logging.warning(f"Couldn't process {add} in .getMaliciousFilesCount() /hostname/../malware api call")
                if(filesCount > limit-1):
                    filesCount = limit
                    break
            except KeyError:
                continue
            except EnvironmentError as err:
                logging.warning(f"ATnTThreatIntel.getMaliciousFilesCount({add}, {limit}) - {err}")
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
        url = self.__getDomain(url)
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
        try:
            req = requests.get(f"https://otx.alienvault.com/api/v1/indicators/domain/{url}/general").json()
            return req["pulse_info"]["count"]
        except KeyError:
            pass
        except EnvironmentError as err:
            logging.warning(f"ATnTThreatIntel.puleCount({url}) - {err}")
        return None
        

    def __checkValidInput(self, url, method):
        """
            Internal method, do not use outside of this class
        """
        if not len(url):
            logging.warning(f"Invalid URL \"{url}\" was given to ATnTThreatIntel{method}")
            return 1
        return 0

    def __getDomain(self, url):
        url = re.split("//", url)[1]
        try:
            url = re.split("w{3}\.", url)[1]
        except IndexError:
            pass
        url = re.split("/", url)[0]
        return url
