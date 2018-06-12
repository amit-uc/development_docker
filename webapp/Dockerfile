FROM alpine:latest

RUN apk add --update python3 && rm -rf /var/cache/apk/*

WORKDIR /app/

ADD requirements.txt /app/requirements.txt

RUN pip3 install -r requirements.txt
