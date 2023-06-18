FROM python:3.11-slim-buster

WORKDIR /usr/app/e_commerce

COPY . .

RUN pip install -r requirements.txt

