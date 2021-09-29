#!/bin/sh

# Apply DB migrations
python manage.py migrate

# Run Django dev't server
python manage.py runserver 0.0.0.0:8080