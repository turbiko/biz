Dockerize 1ver

https://github.com/phookycom/wagtailondocker

https://www.phooky.com/blog/dockerize-wagtail-postgresql-as-a-development-environment/

docker-compose up -d --build

docker-compose exec web python manage.py createsuperuser --settings=biz.settings.dev