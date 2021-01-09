FROM python:3.8.1-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /usr/src/app/requirements.txt

RUN set -eux \
  && apk add --no-cache --virtual .build-deps build-base \
    libressl-dev libffi-dev gcc musl-dev python3-dev \
  && pip install --upgrade pip setuptools wheel \
  && pip install -r /usr/src/app/requirements.txt \
  && rm -rf /root/.cache/pip

RUN apk --purge del .build-deps  

COPY . /usr/src/app/
