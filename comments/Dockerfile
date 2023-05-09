FROM python:3.9-alpine
RUN apk update && apk add --no-cache build-base mysql-client mysql-dev
RUN pip install passlib mysqlclient
RUN pip3 install PyJWT

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .