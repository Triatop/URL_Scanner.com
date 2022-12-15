from datetime import date
import psycopg2
import re
import hashlib, uuid
import json
from UrlController import UrlController

class DBController:
    def __init__(self):
        try:
            with open('settings.json', 'r') as json_file:
                settings = json.load(json_file)
            self.conn = psycopg2.connect(
                host = settings['host'],
                dbname = settings['dbname'],
                user = settings['user'],
                password = settings['password'],
                port = settings['port']
            )
            self.cur = self.conn.cursor()
            self.user_value = 7015
        except (Exception, psycopg2.Error) as error:
            print("Error occured while connecting to database:", error)
            print("Make sure the database is up and running")
    
    def getUrlAttributes(self):
        try:
            url_ctrl = UrlController()
            query = '''select en_url, attributes  from scans'''
            self.cur.execute(query)
            self.conn.commit()
            url_attr_lst = list([[r[0], r[1]] for r in self.cur.fetchall()])
            for index, val in enumerate(url_attr_lst):
                url_attr_lst[index][0] = url_ctrl.decryptUrl(val[0])
            return url_attr_lst
        except (Exception, psycopg2.Error) as error:
            self.conn.rollback()
            print("Error occured while fetching attributedicts:", error)
    
    #Created for demo version
    def getPrevScans(self):
        try:
            url_ctrl = UrlController()
            query = '''select en_url, s_value, attributes, site_age, mal_links, char_swap_url from scans'''
            self.cur.execute(query)
            self.conn.commit()
            url_attr_lst = list({'url': r[0], 's_value': r[1], 'attributes': r[2], 'site_age': r[3], 'mal_links': r[4], 'char_swap_url': r[5]} for r in self.cur.fetchall())
            for index, val in enumerate(url_attr_lst):
                url_attr_lst[index]['url'] = url_ctrl.decryptUrl(val['url'])
            return url_attr_lst
        except (Exception, psycopg2.Error) as error:
            self.conn.rollback()
            print("Error occured while fetching previous scans:", error)

    def getAllUsernames(self):
        query = '''select users.username  from scans left join users on scans.user_id = users.user_id where scans.user_id is not null group by scans.user_id, users.username'''
        self.cur.execute(query)
        self.conn.commit()
        return list([r[0] for r in self.cur.fetchall()])
    
    def check_password(self, password, salt, en_pw):
        return hashlib.sha512(password.encode('utf-8') + salt.encode('utf-8')).hexdigest() == en_pw
    
    def hash_password(self, password):
        salt = uuid.uuid4().hex
        hashed_password = hashlib.sha512(password.encode('utf-8') + salt.encode('utf-8')).hexdigest()
        return salt, hashed_password

    def loginUser(self, username, password):
        try:
            query = '''select en_pw, salt from users where username = '{}' '''.format(username)
            self.cur.execute(query)
            self.conn.commit()
            fetch = self.cur.fetchall()[0]
            en_pw = fetch[0]
            salt = fetch[1]
            return self.check_password(password, salt, en_pw)
        except (Exception, psycopg2.Error) as error:
            self.conn.rollback()
            print("Error occured while logging in user:", error)

    def getUserToken(self, username):
        try:
            query = '''select access_token from users where username = '{}' '''.format(username)
            self.cur.execute(query)
            self.conn.commit()
            return self.cur.fetchone()[0]    
        except(Exception, psycopg2.Error) as error:
            self.conn.rollback()
            print("Error occured while fetching User Token:", error)

    def getHistory(self, username):
        try:
            u_id = self.getUserId(username)
            query = '''select en_url , "date", s_value, attributes, site_age, mal_links, char_swap_url  from scans where user_id = %s order by scan_id DESC;'''
            self.cur.execute(query, str(u_id))
            self.conn.commit()
            return self.cur.fetchall()
        except (Exception, psycopg2.Error) as error:
            self.conn.rollback()
            print("Error occured while fetching history:", error)
        

    def authenticateAdmin(self, username):  
        try:
            query = '''select rights_name from users inner join rights on users.rights_id = rights.rights_id and users.username = '{}' '''.format(username)
            self.cur.execute(query)
            self.conn.commit()
            return self.cur.fetchone()[0] == 'admin'
        except (Exception, psycopg2.Error) as error:
            self.conn.rollback()
            print("Error occured while authenticating admin:", error)
            return False

    def checkUsernameExists(self, username):
        try:        
            query = '''select count(*) from users where username='{}' '''.format(username)
            self.cur.execute(query)
            self.conn.commit()
            return self.cur.fetchone()[0] == 1
        except (Exception, psycopg2.Error) as error:
            self.conn.rollback()
            print("Error occured while checking existing usernames:", error)
            return False

    def createUser(self, username, password, fullname, a_token, admin_priv):
        name_split = fullname.split(' ')
        fname = ''
        lname = ''
        if(len(name_split) > 1):
            fname = name_split[0]
            lname = name_split[1]
        else:
            fname = name_split[0]

        salt, en_pw = self.hash_password(password)
        rg_date = date.today()
        try:
            if(admin_priv): self.user_value = 3681
            query = '''insert into users(rights_id, username, en_pw, salt, fname, lname, rg_date, access_token) values('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')'''.format(self.user_value, username, en_pw, salt, fname, lname, rg_date, a_token)
            self.cur.execute(query)
            self.conn.commit()      
        except (Exception, psycopg2.Error) as error:
            self.conn.rollback()
            print("Error occured while creating user:", error)
    
    def validateUser(self, uname, token): #username and token
        try:
            query = '''select count(*) from users where username = '{}' and access_token = '{}' '''.format(uname, token)
            self.cur.execute(query)
            self.conn.commit()
            return self.cur.fetchone()[0] == 1
        except (Exception, psycopg2.Error) as error:
            self.conn.rollback()
            print("Error occured while validating username and token:", error)
            return False

    def getUserId(self, username):
        try:
            if(username == ''):
                return None        
            query = '''select user_id from users where username='{}' '''.format(username)
            self.cur.execute(query)
            self.conn.commit()
            return self.cur.fetchone()[0]
        except (Exception, psycopg2.Error) as error:
            self.conn.rollback()
            print("Error occured while checking for existing user ID:", error) 
            return None 

    def insertScan(self, username, url, s_value, a_dict, site_age, mal_links, char_swap_url):
        user_id = self.getUserId(username)
        try:        
            query = ''' insert into scans(user_id, en_url, date, s_value, attributes, site_age, mal_links, char_swap_url) values(%s, %s, CURRENT_DATE, %s, %s, %s, %s, %s)  '''
            self.cur.execute(query, (user_id, url, s_value, json.dumps(a_dict), site_age, mal_links, char_swap_url))
            self.conn.commit()
        except (Exception, psycopg2.Error) as error:
            self.conn.rollback()
            print("Error occured while inserting Scan:", error) 
    
    def setupDB(self):
        try:
            query = '''drop table if exists rights, scans, users'''
            self.cur.execute(query)
            self.conn.commit()
        except (Exception, psycopg2.Error) as error:
            self.conn.rollback()
            print("Error occured while dropping tables:", error)

        try:
            query1 = '''CREATE TABLE rights (rights_id int primary key,
                        rights_name varchar(10) not null
                        )'''
            self.cur.execute(query1)
            self.conn.commit()

            query2 = '''CREATE TABLE users (
                        user_id serial primary key,
                        rights_id int not null,
                        username VARCHAR ( 50 ) UNIQUE NOT NULL,
                        en_pw VARCHAR ( 255 ) NOT NULL,
                        salt VARCHAR (255) NOT NULL,
                        fname VARCHAR (50) NOT NULL,
                        lname VARCHAR (50) NULL,
                        rg_date date NOT NULL,
                        access_token VARCHAR (255) NOT null,
                        foreign key (rights_id) references rights(rights_id)
                        )'''
            self.cur.execute(query2)
            self.conn.commit()

            query3 = '''CREATE TABLE scans (
                    scan_id serial primary key,
                    user_id int NULL,
                    en_url VARCHAR ( 255 ) NOT NULL,
                    date DATE NOT NULL,
                    s_value BOOLEAN NOT NULL,
                    attributes jsonb NOT NULL,
                    site_age int NOT NULL,
                    mal_links int NOT NULL,
                    char_swap_url VARCHAR ( 255 ),
                    foreign key (user_id) references users(user_id)
                    )'''
            self.cur.execute(query3)
            self.conn.commit()

            query4 = '''INSERT INTO rights
                    (rights_id, rights_name)
                    VALUES ( 3681, 'admin' )'''
            self.cur.execute(query4)
            self.conn.commit()

            query5 = '''INSERT INTO rights
                    (rights_id, rights_name)
                    VALUES ( 7015, 'regUser' )'''
            self.cur.execute(query5)
            self.conn.commit()

            print('\nDatabase created successfully with existing admin account:\nUsername: admin\nPassword: admin\n')

            values = ('32f1ac0c1b4ea8ef16cd73ef7d6203dbbc640a0a8083a5a1d4c4c49b9026cbb04b530fd15636e012bf6c55c087840ba27acd371c80074537b0027d2996e68f48',
                        'f266f35bcd2e41ff81e3e148eac2bbc0', '$2a$10$mWp.O9mewMpC3gJLU5THN.jRTnr7D/kCfTc0NH.LkJwu/B69Ysuou')
            query6 = '''INSERT INTO users
                        ( rights_id, username, en_pw, salt, fname, lname, rg_date, access_token)
                        VALUES ( 3681, 'admin', %s, %s, 'admin', 'admin', CURRENT_DATE, %s)'''
            self.cur.execute(query6, values)
            self.conn.commit()
        except(Exception, psycopg2.Error) as error:
            self.conn.rollback()
            print("Error occured while setting up DB:", error)

if __name__ == "__main__":
    db_obj = DBController()
    db_obj.setupDB()
