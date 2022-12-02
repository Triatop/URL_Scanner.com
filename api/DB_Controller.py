from datetime import date
import psycopg2
import re
import hashlib, uuid
import json

class DBController:
    def __init__(self):
        try:
            self.conn = psycopg2.connect(
                host = 'localhost',
                dbname = 'postgres',
                user = 'postgres',
                password = 'url_scanner1',
                port = 5432
            )
            self.cur = self.conn.cursor()
            self.user_value = 2011
        except (Exception, psycopg2.Error) as error:
            print("Error occured while connecting to database", error)
        
    def getAllUsernames(self):
        query = '''select users.username  from scans left join users on scans.user_id = users.user_id group by scans.user_id, users.username'''
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
            print("Error occured while logging in user", error)

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
            query = '''select en_url , "date", s_value  from scans where user_id = %s;'''
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
            print("Error occured while authenticating admin", error)

    def checkUsernameExists(self, username):
        try:        
            query = '''select username from users where username='{}' '''.format(username)
            self.cur.execute(query)
            self.conn.commit()
            return self.cur.fetchone()[0] == username
        except (Exception, psycopg2.Error) as error:
            self.conn.rollback()
            print("Error occured while checking existing usernames", error)

    def createUser(self, username, password, fullname, a_token, admin_priv):
        name_split = fullname.split(' ')
        fname = ''
        lname = ''
        if(len(name_split) == 2):
            fname = name_split[0]
            lname = name_split[1]
        else:
            fname = name_split[0]

        salt, en_pw = self.hash_password(password)
        rg_date = date.today()
        try:
            if(admin_priv): self.user_value = 2007
            query = '''insert into users(rights_id, username, en_pw, salt, fname, lname, rg_date, access_token) values('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')'''.format(self.user_value, username, en_pw, salt, fname, lname, rg_date, a_token)
            self.cur.execute(query)
            self.conn.commit()      
        except (Exception, psycopg2.Error) as error:
            self.conn.rollback()
            print("Error occured while creating user", error)
    
    def validateUser(self, uname, token): #username and token
        try:
            query = '''select count(*) from users where username = '{}' and access_token = '{}' '''.format(uname, token)
            self.cur.execute(query)
            self.conn.commit()
            return self.cur.fetchone()[0] == 1
        except (Exception, psycopg2.Error) as error:
            self.conn.rollback()
            print("Error occured while validating username and token:", error)

    def getUserId(self, username):
        try:        
            query = '''select user_id from users where username='{}' '''.format(username)
            self.cur.execute(query)
            self.conn.commit()
            return self.cur.fetchone()[0]
        except (Exception, psycopg2.Error) as error:
            self.conn.rollback()
            print("Error occured while checking for existing user ID:", error) 
            return None 

    def insertScan(self, username, url, s_value, a_dict):
        user_id = self.getUserId(username)
        try:        
            query = ''' insert into scans(user_id, en_url, date, s_value, attributes) values(%s, %s, CURRENT_DATE, %s, %s)  '''
            self.cur.execute(query, (user_id, url, s_value, json.dumps(a_dict)))
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
                    foreign key (user_id) references users(user_id)
                    )'''
            self.cur.execute(query3)
            self.conn.commit()

            query4 = '''INSERT INTO rights
                    (rights_id, rights_name)
                    VALUES ( 2007, 'admin' )'''
            self.cur.execute(query4)
            self.conn.commit()

            query5 = '''INSERT INTO rights
                    (rights_id, rights_name)
                    VALUES ( 2011, 'regUser' )'''
            self.cur.execute(query5)
            self.conn.commit()

            print('database done')

            values = ('32f1ac0c1b4ea8ef16cd73ef7d6203dbbc640a0a8083a5a1d4c4c49b9026cbb04b530fd15636e012bf6c55c087840ba27acd371c80074537b0027d2996e68f48',
                        'f266f35bcd2e41ff81e3e148eac2bbc0', '$2a$10$mWp.O9mewMpC3gJLU5THN.jRTnr7D/kCfTc0NH.LkJwu/B69Ysuou')
            query6 = '''INSERT INTO users
                        ( rights_id, username, en_pw, salt, fname, lname, rg_date, access_token)
                        VALUES ( 2007, 'admin', %s, %s, 'admin', 'admin', CURRENT_DATE, %s)'''
            self.cur.execute(query6, values)
            self.conn.commit()
        except(Exception, psycopg2.Error) as error:
            self.conn.rollback()
            print("Error occured while setting up DB:", error)

    def __del__(self):
        if self.cur is not None:
            self.cur.close()
        if self.conn is not None:
            self.conn.close()

if __name__ == "__main__":
    db_obj = DBController()
    db_obj.setupDB()
