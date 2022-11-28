from datetime import date
import psycopg2
import re


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

    def format(self, string): 
        return re.sub('[^A-Za-z0-9]+', '', str(string))
    
    def authenticateUser(self, username, user_token):
        pass

    def getUserToken(self):
        pass

    def getHistory(self):
        pass

    def authenticateAdmin(self, username):  
        query = '''select rights_name from users inner join rights on users.rights_id = rights.rights_id and users.username = '{}' '''.format(username)
        self.cur.execute(query)
        self.conn.commit()
        return self.format(self.cur.fetchone()) == 'admin'

    def checkUsernameExists(self, username):
        try:        
            query = '''select username from users where username='{}' '''.format(username)
            self.cur.execute(query)
            self.conn.commit()
            return self.format(self.cur.fetchone()) == username
        except (Exception, psycopg2.Error) as error:
            print("Error occured while checking existing usernames", error)

    def createUser(self, username, en_pw, salt, fname, lname):
        rg_date = date.today()
        try:    
            query = '''insert into users(rights_id, username, en_pw, salt, fname, lname, rg_date) values('{}', '{}', '{}', '{}', '{}', '{}', '{}')'''.format(self.user_value, username, en_pw, salt, fname, lname, rg_date)
            self.cur.execute(query)
            self.conn.commit()      
        except (Exception, psycopg2.Error) as error:
            print("Error occured while creating user", error)
            
    def __del__(self):
        if self.cur is not None:
            self.cur.close()
        if self.conn is not None:
            self.conn.close()
    
o = DBController()
print(o.createUser())
del o