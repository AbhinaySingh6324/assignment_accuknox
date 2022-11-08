FROM python:3

ADD . /app

WORKDIR /app

CMD ["python","maintask1.py"]