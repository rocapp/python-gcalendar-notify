#!/bin/bash

## Set necessary environment variables for python-gcal-notify

# path to google api credentials
export pygcal_credentials="/home/${USER}/.gcalendar-creds.json"

# path to the root directory (contains this file, the pygcal .py file, etc)
export pygcal_root_path="/home/${USER}/Git/python-gcalendar-notify/"

# path to python3 (for which 'requirements.txt' has been installed), in this case a local virtual environment
export pygcal_python_path="${pygcal_root_path}pygcal/bin/python3"

# path to pygcal .py file to be executed
export pygcal_exe_path="${pygcal_root_path}pygcal-notify.py"
