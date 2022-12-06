# URL_Scanner.com

SBOM:
* requests : []
* re : []
* logging : []
* ssl : []
* socket : ['gethostbyname']
* certifi : []
* unidecode : ['unidecode']
* csv : []
* json : []
* func_timeout : []
* threading : []
* os : []
* pandas : []
* datetime : ['date', 'date', 'datetime,', 'timedelta']
* psycopg2 : []
* hashlib, : []
* flask : ['Flask,', 'request']
* time : []
* flask_cors : ['CORS']
* urllib : []
* math : []
* serviceping : []
* keras.models : ['load_model', 'Sequential,', 'load_model']
* platform : []
* urllib.parse : ['urlparse']
* keras.layers : ['Dense']
* sklearn.model_selection : []
* sklearn.metrics : ['accuracy_score,', 'f1_score,', 'precision_score,', 'recall_score']
* random : []
* string : []
* cryptography.fernet : []
* requests_html : ['HTMLSession']
* whois : []
* bs4 : ['BeautifulSoup']


Required packages:
 * pip install pytest (For automated testing only)
 * pip install requests_html
 * pip install sockets
 * pip install flask
 * pip install psycopg2
 * pip install python-whois
 * pip install bs4
 * pip install python-whois
 * pip install -U flask-cors
 * pip install unidecode
 * pip install serviceping


Setup Instructions:
 * Install python3 via https://www.python.org/downloads/, recommended version 3.10.8 since 3.11 does not have all dependencies yet.
   Also make sure that python is in the "path" so that it can be accessed anywhere.
 * Install node via https://nodejs.org/en/download/, latest version possible.
 * Run npm install -g yarn
 * Try to run the command "pip" in the terminal, if it's not reccognized as a command, then copy the content of https://raw.githubusercontent.com/pypa/get-pip/main/public/get-pip.py and paste into a new file the with extention ".py" and run with python.
 * Run "pip install -r pipRequirements.txt" while being in the URL_Scanner.com directory and all the python dependencies are installed.
 * To run the program, make sure to be in the URL_Scanner.com directory and run the command "yarn start" and in another terminal run "yarn start-api".

Setup database instructions:
 * Download the latest version of postsgresql at "https://www.enterprisedb.com/downloads/postgres-postgresql-downloads"
 * Install postgresql (Be sure to include pgAdmin 4 if you don't have it already).
 * Create the database in pgAdmin using these parameters: {host = 'localhost', dbname = 'postgres', user = 'postgres', password = 'url_scanner1', port = 5432}
 * Run the file /api/DB_Controller.py
