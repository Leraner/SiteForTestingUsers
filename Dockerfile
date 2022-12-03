FROM python:3.9.15

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /home/SiteForTestingUsers

# TODO: Error in celery with tensorflow (finding image)

COPY requirements1.txt requirements.txt
RUN pip3 install -r requirements.txt

RUN pip3 install drf_yasg
RUN pip3 install django_celery_results
RUN pip3 install psycopg2
RUN pip3 install opennsfw2

COPY ./TestingUsers/. /home/SiteForTestingUsers/TestingUsers/

WORKDIR /home/SiteForTestingUsers/TestingUsers