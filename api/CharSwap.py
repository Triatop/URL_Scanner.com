import re
from unidecode import unidecode
import csv

class CharSwap:
    def __init__(self):
        self.c_url = ''
        self.c_NumPos = []
        self.sus_url = ''
    
    def getData(self, i_url):
        self.c_url = list(filter(None, i_url.split('/')))[1]
        return 1

    def stripWWW(self):
        if list(filter(None, self.c_url.split('.')))[0] == 'www':
            s_list = list(filter(None, self.c_url.split('.')))
            temp = ''
            for i in range(len(s_list)-1):
                if temp != '': temp += '.'
                temp += s_list[i+1]

            self.c_url = temp
            self.sus_url = self.c_url
            return 1
        else:
            self.sus_url = self.c_url
            return 0

    def checkSC(self):     #Special cases wont get caught in stripAccents or will be mistranslated 
        sc_Check = re.compile('[01569ŋ]+') #exceptions that do not get stripped away. 
        sc_arr = sc_Check.findall(self.sus_url)
        if len(sc_arr) != 0:
            self.sus_url = self.sus_url.replace('6', 'b')
            self.sus_url = self.sus_url.replace('9', 'g')
            self.sus_url = self.sus_url.replace('1', 'l')
            self.sus_url = self.sus_url.replace('ŋ', 'n')
            self.sus_url = self.sus_url.replace('0', 'o')
            self.sus_url = self.sus_url.replace('5', 's')
            return 1

        else: return 0

    def stripAccents(self):
            self.sus_url = unidecode(self.sus_url)
            return 1

    def isTop500(self):
        reader = csv.reader(open('top500Domains.csv'))
        found = 0
        for line in reader:
            if self.sus_url == line[0]:
                found = 1
                break
        return found

    def isCharSwap(self):
        bamboozle = 0
        self.stripWWW()
        self.checkSC()
        self.stripAccents()
        if(self.c_url != self.sus_url):
            if(self.isTop500() == 1):
                bamboozle = 1
        return bamboozle