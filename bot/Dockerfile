#Dockerfile for aiogram bot
FROM python:3.12.2-alpine3.15

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /bot
WORKDIR /bot
COPY ./bot /bot

RUN adduser -D user
USER user