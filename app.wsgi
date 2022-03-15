#!/usr/bin/python3
import sys
sys.path.insert(0, '/var/www/PatientHistory')

activate_this = '/home/ubuntu/.local/share/virtualenvs/PatientHistory-MEBPlinH/bin/activate_this.py'

with open(activate_this) as file_:
   exec(file_.read(), dict(__file__=activate_this))

from app import app as application
