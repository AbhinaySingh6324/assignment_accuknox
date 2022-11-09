#FROM ubuntu:latest
FROM python:alpine3.7
#RUN  apt  update
#RUN  apt  install  python3 -y
RUN   pip install  pytest


WORKDIR /usr/app/src



COPY maintask1.py ./
COPY Accuknox2.txt ./
COPY Accuknox3.txt ./
COPY Accuknox.txt ./
COPY test.py ./

ENTRYPOINT [ "python3", "./maintask1.py"]
CMD  ["pytest", "./test.py"]
#RUN  pytest test.py