# Foodgram

На этом сервисе пользователи могут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.

## Используемые технологии:

- #### Django
- #### DRF
- #### Postgres
- #### Nginx
- #### Docker Compose
- #### React

## Запуск в dev-режиме

#### Из директории infra выполните команду
```
docker-compose -f docker-compose-local.yml up -d
```

#### Выполните миграции и сбор статики
```bash
docker exec -it <имя> python manage.py migrate
docker exec -it <имя> python manage.py collectstatic
```
#### Создайте суперюзера и загрузите данные в базу данных
```bash
docker exec -it <имя> python manage.py createsuperuser
docker exec -it <имя> python manage.py load_tags_json
docker exec -it <имя> python manage.py load_ingredients_csv
```

#### Сервис Foodgram будет доступен по адресу в браузере: http://localhost/

#### Документация по API будет доступна по адресу: http://localhost/api/docs/

#### Панель администрирования будет доступна по адресу: http://localhost/admin/


## Деплой на удаленный сервер

#### Секреты CI/CD
```
# В Settings - Secrets and variables - Actions 
добавьте secrets c вашими данными в репозиторий на гитхаб:

DOCKER_USERNAME
DOCKER_PASSWORD
HOST
USER
SSH_KEY
SSH_PASSPHRASE
DB_ENGINE
DB_NAME
POSTGRES_USER
POSTGRES_PASSWORD
DB_HOST
DB_PORT
TELEGRAM_TO
TELEGRAM_TOKEN
```
#### Покдлючитесь к удаленному серверу
```
ssh username@server_ip
```
#### Следующая команда совершает 3 действия:
Обновите список доступных пакетов и их версии из основных репозиториев, установите обновления для всех установленных пакетов и установите пакет curl.
```
sudo apt update && sudo apt upgrade -y && sudo apt install curl -y
```
#### Установка и настройка Docker
```bash
sudo curl -fsSL https://get.docker.com -o get-docker.sh && sudo sh get-docker.sh && sudo rm get-docker.sh

sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

sudo chmod +x /usr/local/bin/docker-compose

sudo systemctl start docker.service && sudo systemctl enable docker.service
```
#### Создайте папку infra и docs
```bash
cd ~
mkdir infra
mkdir docs
```
#### Перенесите файлы docker-compose.yml, nginx.conf и .env, openapi-chema.yml и redoc.html с вашего ПК на сервер.
Не забудьте добавить ip сервера в server_name в файле с настройками nginx
```
scp docker-compose.yml username@server_ip:/home/username/infra/
scp nginx.conf username@server_ip:/home/username/infra/
scp .env username@server_ip:/home/username/infra/
scp openapi-chema.yml username@server_ip:/home/username/docs/
scp redoc.html username@server_ip:/home/username/docs/
```

#### На своем ПК соберите образы для backend и frontend, запушьте их на DockerHub и измените docker-compose под свои образы.
Не забудьте добавить ip сервера в CSRF_TRUSTED_ORIGINS и ALLOWED_HOSTS
```bash
docker login
docker build -t username/название_образа:latest .
docker push username/название_образа:latest
```
#### На удаленном сервере перейдите в папку infra и выполните команду
```bash
sudo docker compose up -d --build
```
####  Выполните миграции, соберите статику, создайте админа и загрузите данные в базу данных

```bash
sudo docker exec -it infra-backend-1 python manage.py migrate
sudo docker exec -it infra-backend-1 python manage.py collectstatic
sudo docker compose exec infra-backend-1 python manage.py createsuperuser
sudo docker exec -it infra-backend-1 python manage.py load_tags_json
sudo docker exec -it infra-backend-1 python manage.py load_ingredients_csv
```
#### Сервис Foodgram будет доступен по адресу: http://server_ip

#### Документация по API будет доступна по адресу: http://server_ip/api/docs/

#### Панель администрирования будет доступна по адресу: http://server_ip/admin/

'''
ip сервера 51.250.22.48
данные учетки администратора: semechkina.n@yandex.ru 2mdhbYPM
'''
