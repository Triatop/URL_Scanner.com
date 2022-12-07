import json
from DB_Controller import DBController



def setup():
    DB_SETUP = False
    while(DB_SETUP == False):
        try:
            setup_dict = {
            'IPQS_key': '',
            'host' : '',
            'dbname' : '',
            'user' : '',
            'password' : '',
            'port' : 0
            }

            #Databse settings
            print('\nPlease insert the settings for your databse:')
            setup_dict['host'] = input('\tHost (ex. localhost): ')
            setup_dict['dbname'] = input('\tDatabase (ex. postgres): ')
            setup_dict['user'] = input('\tUsername (ex. postgres): ')
            setup_dict['password'] = input('\tPassword: ')
            setup_dict['port'] = int(input('\tPort (ex. 5432): '))

            #IPQS settings
            print('\nPlease insert the API-key for the IPQualityScore API:')
            setup_dict['IPQS_key'] = input('\tAPI-key: ')
            with open('settings.json', 'w') as setup_json:
                json.dump(setup_dict, setup_json, indent=4)
            setup_json.close()
            
            db_obj = DBController()
            db_obj.setupDB()
            
            DB_SETUP = True            
        except:
            print('Could not create the databse... \nTry inserting the correct settings for the database.')
    

if __name__ == "__main__":
    setup()