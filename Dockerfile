FROM python:alpine
MAINTAINER Bryce Thomsen
ADD . /jiracli
ADD . setup.py
RUN python3 setup.py install
CMD jiracli

