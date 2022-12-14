import requests
import urllib
import json
import math

class MaliciousLinks:
    def __init__(self):
        with open('settings.json', 'r') as json_file:
            api_key = json.load(json_file)['IPQS_key']

        self.m_links = []
        self.m_DupCount = []
        self.m_url = ''
        self.m_apiKey = api_key #Go into 'settings.json' and insert the key there if you dont wanna run setup.py
        self.m_NrOfMalLinks = 0

    def getNrOfMalLinks(self):
        return self.m_NrOfMalLinks
        
    def getData(self, i_url, i_links):
        self.m_links = i_links
        self.m_url = list(filter(None, i_url.split('/')))[1]      #get top level domains of the list trim off protocol and anything after
        return 1

    def externalCheck(self):
        f_iterations = len(self.m_links)
        i = 0
        while(i < f_iterations):
            try:
                if self.m_links[i][0] == '/' and self.m_links[i][1] != '/': #/link är en intern länk
                    self.m_links.pop(i)
                    i -= 1
                    f_iterations -= 1  
                else:
                    if self.m_links[i][0] == '/' and self.m_links[i][1] == '/': #// is URL with a relative (unspecified) protocol
                        self.m_links[i] = self.m_links[i].replace('//', 'https://', 1)  #specify the protocol
                        
                    comProt = list(filter(None, self.m_links[i].split('/')))[0]
                    compare = list(filter(None, self.m_links[i].split('/')))[1] #Divide and take TLD Example "www.google.com"
                    if self.m_url == compare:                                   #If it is the same level domain as the website our tool is checking.
                        self.m_links.pop(i)
                        i -= 1
                        f_iterations -= 1      
                    elif comProt != 'http:' and comProt != 'https:':        #Not an external link
                        self.m_links.pop(i)                                 #Remove the offending non-link
                        i -= 1                                              #step back one to not mess up i+1
                        f_iterations -= 1                                   #Adjust iterations to match new list size

            except:                                                         #Has no "/" or is not a link Example "garykessler@gmail.com"
                self.m_links.pop(i)                                         #Remove the offending non-link
                i -= 1                                                      #step back one to not mess up i+1
                f_iterations -= 1                                           #Adjust iterations to match new list size
            i += 1                                                          #check next link
        #print(self.m_links)
        return 1

    def removeDup(self):
        f_it = len(self.m_links)                                          #The last link will always be unique
        i = 0
        while i < f_it:
            j = i + 1
            self.m_DupCount.append(1)
            icompare = list(filter(None, self.m_links[i].split('/')))[1]        #The tld you compare to the rest of them
            while j < f_it:                                                     #Nestled while loop :O
                jcompare = list(filter(None, self.m_links[j].split('/')))[1]
                if icompare == jcompare:
                    self.m_links.pop(j)
                    self.m_DupCount[i] += 1
                    f_it -= 1                                                   #1 less iteration
                    j -= 1                                                      #Set back pointer to not skip anything in the next row
                j += 1                                                          #set forward pointer
            i += 1                                                              #Compare next link to the rest of them
        return 1

    def maliciousCheck(self):      #Send an array of links to IP Quality Score and get the response
        self.externalCheck()
        self.removeDup()
        l_response = []
        f_iterations = len(self.m_links)
        s_throttle = False
        if f_iterations > 10:
            f_iterations = 10
            s_throttle = True
            temp = []
        for i in range(f_iterations):
            if s_throttle: temp.append(self.m_DupCount[i])
            try:
                v_url = 'https://www.ipqualityscore.com/api/json/url/%s/%s' % (self.m_apiKey, urllib.parse.quote_plus(self.m_links[i]))  #IPQS url
                m_response = requests.get(v_url)
                #print(m_response.text)
                l_response.append(json.loads(m_response.text))
            except ValueError as e:                                 #when unexpected values are returned
                print("Rate Limit detected:", e)
                print(self.m_links[i])
        if s_throttle:
           print('Too many external links. Checking ' ,f_iterations ,' of them')
           self.m_DupCount = temp
        return l_response

    def isExternalSafe(self):  #Parse the value from IPQS 
        m_extLinks = 0                                      #The value we send back to the object
        m_sum = 0                                           #Sum of all risk scores
        m_lrgi = 0                                          #The position in the score array with the largest score
        m_resp = self.maliciousCheck()                      #The response from malicious check
        r_score = []                                        #An array of the threat scores provided by IPQS
        for i in range(len(m_resp)):
            r_score.append(int(m_resp[i]['risk_score']) * self.m_DupCount[i])    #"risk_score":0, * ammount of duplicates of a link with the same TLD
            m_sum += r_score[i] * self.m_DupCount[i]                             #keep a sum of how bad the links are
            if r_score[i] > 54:                                                  #55 is considered suspicious
                self.m_NrOfMalLinks += self.m_DupCount[i]
            if r_score[m_lrgi] < r_score[i] :
                m_lrgi = i                                  #keep ahold of the worst link
        #print(m_sum, m_lrgi)
        #print(self.m_links[m_lrgi])
        #print(self.m_DupCount)
        #print(r_score)

        if m_sum > 0:                                       #IPQS USES	Overall threat score from: 0 (clean) to 100 (high risk)
            m_extLinks = math.floor(math.ceil(m_sum/sum(self.m_DupCount))/10)  #The mean value of all the threat scores rounded up. Divided by 10 and rounded down to give a score between 0 and 10. 
        return m_extLinks