#!/usr/bin/python3
import sys

# Declare the path of our website data
sys.path.insert(0, '/var/www/PatientHistory')

# Please insert your virtual environment path generated from pipenv
# Activates the environment
activate_this = '<virtual_environment_path>/bin/activate_this.py'

# Execute the activated file
with open(activate_this) as file_:
   exec(file_.read(), dict(__file__=activate_this))

# Imports our main flask app
from app import app as application
