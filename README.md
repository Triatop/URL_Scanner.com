# URL_Scanner.com

SBOM:
* requests
* re
* logging
* ssl
* socket
* certifi
* unidecode
* csv
* json
* func_timeout
* threading
* os
* pandas
* datetime
* psycopg2
* hashlib
* flask
* time
* flask_cors
* urllib
* math
* serviceping
* keras.models
* platform
* urllib.parse
* keras.layers
* sklearn.model_selection
* sklearn.metrics
* random
* string
* cryptography.fernet
* requests_html
* whois
* bs4


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
 * If you are running an M1 mac, run the command "pip install -r pipRequirements-m1.txt" otherwise run 
 "pip install -r pipRequirements.txt" while being in the URL_Scanner.com directory and all the python dependencies are installed.
 * To run the program, make sure to be in the URL_Scanner.com directory and run the command "yarn start" and in another terminal run "yarn start-api".


Setup database and IPQS instructions:
 * Download the latest version of postsgresql at "https://www.enterprisedb.com/downloads/postgres-postgresql-downloads"
 * Install postgresql (Be sure to include pgAdmin 4 if you don't have it already for an easier setup).
 * Make a database connection and write down the follwing settings {Host, Port, Database-name, Username, Password}
 * Make sure the database is up and running - and that the connection went through.
 * Create an account at IP Quality Score's website: https://www.ipqualityscore.com/
 * Log in and go to the page: https://www.ipqualityscore.com/documentation/malicious-url-scanner-api/overview
 * Scroll down untill you see 'Private Key' and write down the API-key.
 * Run the command 'cd api && python setup.py && cd ..' or 'yarn setup' in the terminal inside this direcotry.
 * Follow the guide in the terminal window and insert the settings for the database and the API-key.
 * To reset the database (for some reason) run the command 'cd api && python DB_Controller.py && cd ..' or 'yarn reset-db'

User instructions:
 * Login by pressing the login button at the top.
 * Enter your login information and press enter or the Log in button.
 * Insert the link you wish to scan in the hotbar and press enter or the scan button.
 * If you wish to do another scan, simply replace the last link with your new one and press scan.
 * You can see your past scans by pressing the History button at the top.
 * In history, you can click on the arrow on your past scans to view additional information about the scan. 
 * If you wish to logout, press Logout at the top and confirm by pressing Yes when prompted.
 * Pressing the toggle in the top right corner will switch between light and dark mode.
 * Pressing the home button will redirected you to the home page. 
