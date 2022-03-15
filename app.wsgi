#!/usr/bin/python3
import sys
sys.path.insert(0, '/var/www/PatientHistory')

# Please insert your virtual environment path generated from pipenv

activate_this = '<virtual_environment_path>/bin/activate_this.py'

with open(activate_this) as file_:
   exec(file_.read(), dict(__file__=activate_this))

from app import app as application
