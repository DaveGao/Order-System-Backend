FROM python:3.5-alpine
LABEL maintainer="longjj"
ENV LANG C.UTF-8

RUN apk add --no-cache bash

ADD . /code
WORKDIR /code/app/

# Install python dependence
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
RUN pip install flask-cors --upgrade

EXPOSE 5000