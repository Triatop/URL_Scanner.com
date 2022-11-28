# URL_Scanner.com

SBOM:
* requests_html
* re
* os
* sockets
* serviceping
* cryptography.fernet
* requests
* flask
* datetime
* psycopg
* CORS
* urllib
* json
* math

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


Setup Instructions:
 * Install python3 via https://www.python.org/downloads/, recommended version 3.10.8 since 3.11 does not have all dependencies yet.
   Also make sure that python is in the "path" so that it can be accessed anywhere.
 * Install node via https://nodejs.org/en/download/, latest version possible.
 * Try to run the command "pip" in the terminal, if it's not reccognized as a command, then copy the content of https://raw.githubusercontent.com/pypa/get-pip/main/public/get-pip.py and paste into a new file the with extention ".py" and run with python.
 * Run "pip install -r pipRequirements.txt" while being in the URL_Scanner.com directory and all the python dependencies are installed.
 * To run the program, make sure to be in the URL_Scanner.com directory and run the command "yarn start" and in another terminal run "yarn start-api".
