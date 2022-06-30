from python:3.10

workdir /app

copy requirements.txt /app/

run pip3 install -r requirements.txt

copy . /app

cmd python3 bot.py
