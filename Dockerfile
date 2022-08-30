FROM python:3.10-slim-bullseye

COPY . /opt/fastapp2
WORKDIR /opt/fastapp2

RUN apt-get update -y
RUN pip install -r requirements.txt
