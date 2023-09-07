# Pet-project
### Образовательная платформа

Образовательная платформа, где каждый пользователь может создать 
свой пост по какой-либо тематике и прикрепить к нему тест.

Например, пользователь может создать пост на тему интегралов, к которому прикрепляется тест на 
усвоение темы интегралов.

Так же на данной платформе запрещено публиковать картинки 18+. Каждая картинка проверяется на содержание 
Not-Suitable-For-Work контента с помощью библиотеки https://github.com/bhky/opennsfw2

### Как запустить проект?
```
git clone https://github.com/Leraner/SiteForTestingUsers.git
pip install -r requirements_conda.txt / pip install -r requirements_virtualenv.txt

### Запускаем в докере rabbitmq ###
docker run -d -p 5672:5672 rabbitmq

### Запускаем celery worker ###
celery -A TestingUsers worker -l INFO

#### В консоле зайти в папку TestingUsers ####
python manage.py migrate
python manage.py prepare_stand
python manage.py runserver

#### В другой консоли заходим в папку testingusers_frontend ####
npm install
npm run serve
```


Docker-compose пока не реализован


Стек, который используется:
* Django Rest Framework
* Celery
* Vue JS
* Opennsfw2 (Tensorflow)
* RabbitMQ
