FROM python:3.12-alpine
LABEL maintainer="eballo"

ENV PYTHONUNBUFFERED=1

COPY ./requirements.txt /requirements.txt

RUN apk add --update --no-cache postgresql-client
RUN pip install --no-cache-dir -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static
RUN adduser -D pythonUser
RUN chown pythonUser:pythonUser -R /app/
RUN chown pythonUser:pythonUser -R /vol/
RUN chmod -R 755 /vol/web
RUN chmod -R 755 /app/
USER pythonUser
