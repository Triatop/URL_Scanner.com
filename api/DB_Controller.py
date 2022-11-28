from datetime import date
import psycopg2

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


    def getUserRights(self, user_id):      
        query = '''select rights_name from users inner join rights on users.rights_id = rights.rights_id and users.user_id = %s'''
        query_values = (user_id)
        self.cur.execute(query, query_values)
        self.conn.commit()
        return self.cur.fetchone()
    
    def __del__(self):
        if self.cur is not None:
            self.cur.close()
        if self.conn is not None:
            self.conn.close()
    
