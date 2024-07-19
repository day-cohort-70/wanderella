#!/bin/bash

rm db.sqlite3
rm -rf ./wanderellaapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations wanderellaapi
python3 manage.py migrate wanderellaapi
python3 manage.py loaddata users
python3 manage.py loaddata tokens
python3 manage.py loaddata user_profiles
python3 manage.py loaddata airlines
python3 manage.py loaddata hotels
python3 manage.py loaddata room_types
python3 manage.py loaddata amenities
python3 manage.py loaddata hotel_amenities
python3 manage.py loaddata flights
python3 manage.py loaddata rental_cars
python3 manage.py loaddata bookings
python3 manage.py loaddata reviews