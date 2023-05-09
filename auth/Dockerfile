FROM python:3.9-alpine
RUN apk update && apk add --no-cache build-base mysql-client mysql-dev
RUN pip install passlib mysqlclient
RUN pip install bcrypt
RUN pip3 install PyJWT

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

COPY requirements.txt /tmp
RUN pip3 install --upgrade pip
RUN pip3 install -r /tmp/requirements.txt
RUN pip install mysqlclient
RUN apk add nmap-ncat


COPY . .