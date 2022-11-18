import requests
import urllib
import json
import math

class MaliciousLinks:
    def __init__(self):
        self.m_links = []
        self.m_url = ''
        self.m_apiKey = '' #Replace with non-personal ID 

    def getData(self, i_url, i_links):
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
            except:                                              #Has no "/" or is not a link Example "garykessler@gmail.com"
                self.m_links.pop(i)                                         #Remove the offending non-link
                i -= 1                                                      #step back one to not mess up i+1
                f_iterations -= 1                                           #Adjust iterations to match new list size
            i += 1                                                          #check next link
        #print(self.m_links)
        return 1

    def removeDup(self):
        f_it = len(self.m_links)-1                                          #The last link will always be unique
        i = 0
        while i < f_it:
            j = i + 1
            icompare = list(filter(None, self.m_links[i].split('/')))[1]        #The tld you compare to the rest of them
            while j < f_it:                                                     #Nestled while loop :O
                jcompare = list(filter(None, self.m_links[j].split('/')))[1]
                if icompare == jcompare:
                    self.m_links.pop(j)
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
        if f_iterations > 50:
            f_iterations = 50
            s_throttle = True
        for i in range(f_iterations):
            try:
                v_url = 'https://www.ipqualityscore.com/api/json/url/%s/%s' % (self.m_apiKey, urllib.parse.quote_plus(self.m_links[i]))  #IPQS url
                m_response = requests.get(v_url)
                #print(m_response.text)
                l_response.append(json.loads(m_response.text))
            except ValueError as e:                                 #when unexpected values are returned
                print("Rate Limit detected:", e)
        if s_throttle: print('Too many external links. Checking 50 of them')
        return l_response

    def isExternalSafe(self):  #Parse the value from IPQS 
        m_extLinks = 0                                      #The value we send back to the object
        m_sum = 0                                           #Sum of all risk scores
        m_lrgi = 0                                          #The position in the score array with the largest score
        m_resp = self.maliciousCheck()                      #The response from malicious check
        r_score = []                                        #An array of the threat scores provided by IPQS
        for i in range(len(m_resp)):
            r_score.append(int(m_resp[i]['risk_score']))    #"risk_score":0,
            m_sum += r_score[i]                             #keep a sum of how bad the links are
            if r_score[m_lrgi] < r_score[i] :
                m_lrgi = i                                  #keep ahold of the worst link
        #print(m_sum, m_lrgi)
        #print(r_score)

        if m_sum > 0:                                       #IPQS USES	Overall threat score from: 0 (clean) to 100 (high risk)
            m_extLinks = math.floor(math.ceil(m_sum/len(m_resp))/10)  #The mean value of all the threat scores rounded up. Divided by 10 and rounded down to give a score between 0 and 10. 
        return m_extLinks
