import serviceping
class PortCheck:
    def __init__(self):
        self.standardPorts = ['443', '80']

    def checkPorts(self, ip):
        for port in self.standardPorts:
            try:
                if(serviceping.scan(ip, port)['state'] == 'open'):
                    return port
            except:
                pass
        return None