#!/bin/bash
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('apterek', 'apterek@mail.ru', '271036yY#')" | python manage.py shell
echo "super user created"
python manage.py runserver 0.0.0.0:8000
