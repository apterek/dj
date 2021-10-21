#!/bin/bash
docker-compose up -d
docker exec dj_django_1 python manage.py migrate
docker exec dj_django_1 sh ./create_test_super_user.sh
docker exec dj_worker_1 python manage.py rqworker default
