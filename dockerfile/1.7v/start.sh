#!/bin/bash

/home/ubuntu/test_web/django_app_config_sh $1 $2 $3 $4 $5 $6

/home/ubuntu/test_web/bin/activate

python container_test_web_django/web_project/manage.py migrate

python container_test_web_django/web_project/manage.py runserver 0:$7