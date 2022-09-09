#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi


python manage.py makemigrations --settings=biz.settings.dev
python manage.py migrate --settings=biz.settings.dev
#python manage.py update_index --settings=biz.settings.dev
gunicorn core.wsgi:application -b :8000
exec "$@"