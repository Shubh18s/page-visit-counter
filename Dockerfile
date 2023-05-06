FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt9999

RUN pip3 install -r requirements.txt

COPY . .

ENV FLASK_APP=visits.py

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=3000"]