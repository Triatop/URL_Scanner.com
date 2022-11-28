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
        except (Exception, psycopg2.Error) as error:
            print("Error occured while connecting to database", error)

    def format(self, string): 
        return re.sub('[^A-Za-z0-9]+', '', str(string))
    
    def authenticateUser(self, username, user_token):
        pass

    def authenticateAdmin(self, username):  
        query = '''select rights_name from users inner join rights on users.rights_id = rights.rights_id and users.username = '{}' '''.format(username)
        query_values = (username)
        self.cur.execute(query, query_values)
        self.conn.commit()
        return 'admin' == self.format(self.cur.fetchone())

    def checkUsernameExists(self, username):
        query = '''select username from users where username='{}' '''.format(username)
        query_values = (username)
        self.cur.execute(query, query_values)
        self.conn.commit()
        return self.format(self.cur.fetchone()) == username
    
    def __del__(self):
        if self.cur is not None:
            self.cur.close()
        if self.conn is not None:
            self.conn.close()
    
o = DBController()
print(o.checkUsernameExists('testusername'))
del o