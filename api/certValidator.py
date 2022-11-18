import ssl
import socket
import certifi
import re

class CertValidator:
    def __init__(self, url = ""):
        self.certLocation = certifi.where()
        self.url = url
    def validateCert(self, url = ""):
        #url = self.url if url == "" else url
        #url = url.split('://')[1] if len(url.split('://')) > 1 else url
        url = re.split("/+", url)[1]
        context = ssl.create_default_context()
        context = ssl.SSLContext(ssl.PROTOCOL_TLS)
        context.verify_mode = ssl.CERT_REQUIRED
        context.check_hostname = True

        context.load_verify_locations(self.certLocation)
        conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname = url)
        try:
            conn.connect((url, 443))
            return 0
        except ssl.SSLCertVerificationError as err:
            return err
        
    def processData(self, url = ""):
        return 0 if self.validateCert(url if url != "" else self.url) else 1
