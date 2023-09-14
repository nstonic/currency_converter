FROM docker.io/python:3.11.3

ENV \
    SECRET_KEY=empty \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off

WORKDIR /opt/app
COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY ./src ./src

WORKDIR /opt/app/src

RUN python manage.py collectstatic --noinput

EXPOSE 8000/tcp

CMD ['python3', 'manage.py', 'runserver', '0.0.0.0:8000']