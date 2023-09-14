# Конвертер валют по курсу ЦБ

## Как развернуть local-окружение

Задайте переменные окружения (можно в файле .env в корне проекта):

```shell
ALLOWED_HOSTS='127.0.0.1, localhost'
DEBUG=True
SECRET_KEY=123456
```

Для запуска ПО вам понадобятся Docker и Docker Compose. Инструкции по их установке ищите на официальных
сайтах:

- [Install Docker Desktop](https://www.docker.com/get-started/)
- [Install Docker Compose](https://docs.docker.com/compose/install/)

Сначала соберите докер-образ с помощью Docker Сompose:

```shell
$ docker compose build
```

Запустите докер-контейнеры:

```shell
$ docker compose up
```


Запуск тестов:
```shell
$ docker compose run --rm django python manage.py test
```

## Как использовать

Конвертировать валюты можно двумя способами: \
[/api/rates/usd/rub/3](http://127.0.0.1:8000/api/rates/usd/rub/3) \
[/api/rates/?from=USD&to=RUB&value=3](http://127.0.0.1:8000/api/rates/?from=USD&to=RUB&value=3) 