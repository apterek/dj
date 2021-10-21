#!/bin/bash
docker-compose up -d
echo "\e[1;33;4;44m Wait up database 10 second \e[0m"
sleep 10s
docker restart dj_django_1 dj_worker_1
docker exec dj_django_1 python manage.py migrate
docker exec dj_django_1 sh ./create_test_super_user.sh
docker exec dj_worker_1 python manage.py rqworker default
