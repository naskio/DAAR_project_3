#!/usr/bin/env bash
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete

rm db.sqlite3

python ./manage.py makemigrations && ./manage.py migrate && ./manage.py createsuperuser --username admin --email admin@gmail.com && ./manage.py loaddata */fixtures/*.json