# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

RUN useradd discord

COPY --chown=discord app /app

USER discord

ENTRYPOINT [ "python3", "/app/app.py"]
