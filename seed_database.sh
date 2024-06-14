#!/bin/bash

rm db.sqlite3
rm -rf ./wanderellaapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations wanderellaapi
python3 manage.py migrate wanderellaapi
python3 manage.py loaddata users
python3 manage.py loaddata tokens

