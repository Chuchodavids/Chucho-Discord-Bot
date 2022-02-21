FROM python:3.8-slim-buster

RUN useradd -ms /bin/bash discord

WORKDIR /home/discord/

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY --chown=discord app app

USER discord

ENTRYPOINT [ "python3", "-u", "/home/discord/app/app.py"]
