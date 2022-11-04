import serviceping
class PortCheck:
    def __init__(self):
        self.standardPorts = {'https' : '443'
                             ,'http' : '80'}

    def checkPorts(self, ip, protocol):
        port = self.standardPorts[protocol]
        try:
            if(serviceping.scan(ip, port)['state'] == 'open'):
                return 1
        except:
            pass
        return 0
