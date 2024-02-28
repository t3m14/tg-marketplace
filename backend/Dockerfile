FROM python:3.12.2-alpine3.15

ENV PYTHONUNBUFFERED 1

COPY./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /backend
WORKDIR /backend
COPY ./backend /backend

RUN adduser -D user
USER user
