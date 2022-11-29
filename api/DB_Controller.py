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

    def loginUser(self, username, password):
        pass

    
    def authenticateUser(self, username, user_token):
        pass

    def getUserToken(self):
        pass

    def getHistory(self):
        pass

    def authenticateAdmin(self, username):  
        try:
            query = '''select rights_name from users inner join rights on users.rights_id = rights.rights_id and users.username = '{}' '''.format(username)
            self.cur.execute(query)
            self.conn.commit()
            return self.format(self.cur.fetchone()) == 'admin'
        except (Exception, psycopg2.Error) as error:
            print("Error occured while authenticating admin", error)

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
    
    def validateUser(self, uname, token): #username and token
        values = (uname, token)
        query = '''select count(*) from users where username = %s and access_token = %s'''
        self.cur.execute(query, values)
        self.conn.commit()
        return self.cur.fetchone()[0] == 1

    def setupDB(self):

        query = '''drop table rights, scans, users'''
        self.cur.execute(query)
        self.conn.commit()

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
                s_value bit NOT NULL,
                attributes jsonb NOT NULL,
                foreign key (user_id) references users(user_id)
                )'''
        self.cur.execute(query3)
        self.conn.commit()

        query4 = '''INSERT INTO rights
                (rights_id, rights_name)
                VALUES ( 1, 'admin' )'''
        self.cur.execute(query4)
        self.conn.commit()

        query5 = '''INSERT INTO rights
                (rights_id, rights_name)
                VALUES ( 2, 'regUser' )'''
        self.cur.execute(query5)
        self.conn.commit()

        values = ('$2a$10$ovfJgA/SxVxsd3NeD3dMneuwYdimPJRdG.77eypo1KTlsgd7YmIYi', '$2a$10$YLXY3KPH3Kr0utTzmo6Eke4rAp8oZW0AQPuhaMkgqvi9GTcuo7Sc6')
        query6 = '''INSERT INTO users
                    ( rights_id, username, en_pw, salt, fname, lname, rg_date, access_token)
                    VALUES ( 1, 'admin', %s, 'salt', 'admin', '', CURRENT_DATE, %s)'''
        self.cur.execute(query6, values)
        self.conn.commit()
