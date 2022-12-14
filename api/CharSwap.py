import re
from unidecode import unidecode
import csv
import logging

class CharSwap:
    def __init__(self):
        self.c_url = ''
        self.c_NumPos = []
        self.sus_url = ''
    
    def getData(self, i_url):
        self.c_url = list(filter(None, i_url.split('/')))[1]
        return 1

    def getsus_url(self):
        if (self.c_url != self.sus_url):
            return self.sus_url
        else:
            return ""

    def stripWWW(self):     #this is so comparison with the websites is possible later
        if list(filter(None, self.c_url.split('.')))[0] == 'www':   #split URL by the dots and check if the first part of the url is 'www'
            s_list = list(filter(None, self.c_url.split('.')))      #save the list
            temp = ''                                               #to be the new URL
            for i in range(len(s_list)-1):
                if temp != '': temp += '.'
                temp += s_list[i+1]                                 #add all the domains and subdomains except www to new URL

            self.c_url = temp                                       #set both OG URL and soon to be modified url
            self.sus_url = self.c_url
            return 1
        else:                                                       #if the first part is not 'www' nothing has to be done
            self.sus_url = self.c_url                               #this has to be done regardless
            return 0

    def checkSC(self):     #Special cases wont get caught in stripAccents or will be mistranslated 
        sc_Check = re.compile('[01569ӏŋр]+') #exceptions that do not get stripped away. 
        sc_arr = sc_Check.findall(self.sus_url)
        if len(sc_arr) != 0:
            self.sus_url = self.sus_url.replace('6', 'b')
            self.sus_url = self.sus_url.replace('9', 'g')
            self.sus_url = self.sus_url.replace('ӏ', 'l')
            self.sus_url = self.sus_url.replace('1', 'l')
            self.sus_url = self.sus_url.replace('ŋ', 'n')
            self.sus_url = self.sus_url.replace('0', 'o')
            self.sus_url = self.sus_url.replace('р', 'p')
            self.sus_url = self.sus_url.replace('5', 's')
            self.sus_url = self.sus_url.replace('ш', 'w')
            return 1

        else: return 0

    def stripAccents(self): #take a character "ö" that has accents (the dots) and transform it "o" to its lookalike character
            self.sus_url = unidecode(self.sus_url)
            return 1

    def isTop500(self):
        found = 0
        try:
            with open('top500Domains.csv') as file_csv:                       #Separate line so we can close later
                reader = csv.reader(file_csv)                   #Read File
        except EnvironmentError as err:
            logging.warning(f"CharSwap.isTop500() - {err}")
        for line in reader:
            if self.sus_url == line[0]:                         #if it exists in list
                found = 1                                       #the website tried to trick us
                break                                           #no need to check the others
        return found

    def isCharSwap(self):               #main function
        bamboozle = 0
        self.stripWWW()
        self.checkSC()
        self.stripAccents()
        if(self.c_url != self.sus_url): #does it have any special chars,
            if(self.isTop500() == 1):   #and if so is it trying to mimic a real website by using them
                bamboozle = 1
        return bamboozle
