FROM python:3.9.15

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /home/SiteForTestingUsers

COPY requirements_virtualenv.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY ./TestingUsers/. /home/SiteForTestingUsers/TestingUsers/

WORKDIR /home/SiteForTestingUsers/TestingUsers