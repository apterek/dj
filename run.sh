#!/bin/bash
docker-compose up -d
echo "\e[1;33;4;44m Wait database \e[0m"
docker exec dj_django_1 sh ./entrypoint.sh
