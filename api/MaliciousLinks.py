import requests
import urllib
import json

class MaliciousLinks:
    def __init__(self):
        self.m_links = []
        self.m_url = ''
        self.m_apiKey = '' #Replace with non-personal ID 

    def getData(self, i_links, i_url):
        self.m_links = i_links
        self.m_url = list(filter(None, i_url.split('/')))[1]      #get top level domains of the list trim off protocol and anything after
        return 1

    def externalCheck(self):
        f_iterations = len(self.m_links)
        i = 0
        while(i < f_iterations):
            try:
                compare = list(filter(None, self.m_links[i].split('/')))[1] #Divide and take TLD Example "www.google.com"
                if self.m_url == compare:                                   #If it is the same level domain as the website our tool is checking.
                    self.m_links.pop(i)
                    i -= 1
                    f_iterations -= 1                                       
            except IndexError:                                              #Has no "/" or is not a link Example "garykessler@gmail.com"
                self.m_links.pop(i)                                         #Remove the offending non-link
                i -= 1                                                      #step back one to not mess up i+1
                f_iterations -= 1                                           #Adjust iterations to match new list size
            i += 1                                                          #check next link
        #print(self.m_links)
        return 1

    def maliciousCheck(self):      #Send an array of links to Virustotal and get the response
        self.externalCheck()
        l_response = []
        v_url = 'https://www.ipqualityscore.com/api/json/url/%s/%s' % (self.m_apiKey, urllib.parse.quote_plus(self.m_links[0]))  #virustotal url  parser.add_argument("-u", "--url-list", help="bulk url analysis")
        
        for i in range(len(self.m_links)):
            try:
                m_response = requests.get(v_url)
                #print(m_response.text)
                l_response.append(json.loads(m_response.text))
            except ValueError as e:
                print("Rate Limit detected:", e)
        return l_response

    def isExternalMalicious(self):  #Parse the value from IPQS 
        m_extLinks = 0
        m_sum = 0
        m_lrgi = 0
        m_resp = self.maliciousCheck()
        r_score = []
        for i in range(len(self.m_links)):
            r_score.append(int(m_resp[i]['risk_score']))    #"risk_score":0,
            m_sum += r_score[i]                             #keep a sum of how bad the links are
            if r_score[m_lrgi] < r_score[i] :
                m_lrgi = i                                  #keep ahold of the worst link
        #print(m_sum, m_lrgi)
        #print(r_score)

        if m_sum > 100 or r_score[m_lrgi] > 75:             # IPQS USES	Overall threat score from: 0 (clean) to 100 (high risk)
            m_extLinks = 1                                  # Do we want binary or severity?
        return m_extLinks
