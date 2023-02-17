FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/new_horizon_project

COPY ./misc/requirements.txt /usr/src/requirements.txt
RUN pip install -r /usr/src/requirements.txt

COPY . /usr/src/new_horizon_project

COPY ./misc/db.sqlite3 /usr/src/new_horizon_project/misc/db.sqlite3
COPY ./misc/db.sqlite3 /usr/src/new_horizon_project/db.sqlite3

RUN chmod 777 /usr/src/new_horizon_project/db.sqlite3

EXPOSE 8000


CMD ["python", "manage.py", "runserver", "127.0.0.1:8000"]