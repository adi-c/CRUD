#!/bin/bash
SCRIPTPATH="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
cd $SCRIPTPATH
python3 manage.py makemigrations >> ~/log
python3 manage.py migrate >> ~/log
python3 manage.py runserver 0.0.0.0:8000 >> ~/log