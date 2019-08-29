[![Build Status](https://travis-ci.org/DJWOMS/oms_cms.svg?branch=master)](https://travis-ci.org/DJWOMS/oms_cms)

OMS CMS
=======

OMS is an open source CMS based on the Django framework, designed for flexibility. 
That allows you to easily expand its functionality. This cms allows you to make a website in minutes. 
You can use the basic template or download from the official site.

[Documentation](https://oms-cms.readthedocs.io/ru/latest/)

- Python => 3.6
- Django => 2
- Postgres == 10

Installation:
-------------

Create virtual environment ::

    python -m venv venv
    
Activate virtual environment

Install CMS ::

    pip install oms-cms
    
Create Project ::

    oms-start
    
Development
-----------

Fork or clone the repository. 
Create the file oms_cms/config/local_settings.py and register the connection to the database.

.. code-block :: python

    # coding = utf-8
    import os
    
    BASE_DIR = os.path.dirname (os.path.dirname (os.path.abspath (__ file__)))
    
    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = 'b0! C @ b! O_ # Fdsf4 #% # regdh @ ana6l2 $ n =! P1ejm @'
    
    DEBUG = True
    
    ALLOWED_HOSTS = ["127.0.0.1", "localhost"]
    
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'DB',
            'USER': 'user',
            'PASSWORD': 'pass',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }


    STATIC_DIR = os.path.join (BASE_DIR, 'static')
    STATIC_URL = '/ static /'
    STATICFILES_DIRS = [os.path.join (BASE_DIR, 'static'),]
    
Install Dependencies ::

    pip install -r req.txt
    
Creating a database and setting up CMS ::

    python manage.py deployOMS
    
Run dev server ::

    python manage.py runserver
    
Commands

Launching the installer ::

    oms-start
    
Creating Migration Files ::

    python manage.py makemigrations
    
Application of migrations ::

    python manage.py migrate
    
Create Super User ::

    python manage.py createsuperuser


OMS - это CMS с открытым исходным кодом, основанная на фреймворке Django, разработанная для гибкости.
Что позволяет вам без проблем расширить ее функционал. 
Данная cms позволяет сделать сайт за считанные минуту. Вы можете использовать базовый шаблон или скачать с официального сайта.


[Документация](https://oms-cms.readthedocs.io/ru/latest/)
 
- Python => 3.6
- Django => 2
- Postgres == 10

Установка:
----------

Создать виртуальное окружение ::

    python -m venv venv
    
Активировать виртуальное окружение

Установить CMS ::

    pip install oms-cms
    
Создать проект ::
    
    oms-start


Разработка
----------

- Сделать форк или клонировать репозиторий
- Создать файл oms_cms/config/local_settings.py и прописать конект к базе

.. code-block:: python

    # coding=utf-8
    import os
    
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = 'b0!c@b!o_#Fdsf4#%#regdh@ana6l2$n=!p1ejm@'
    
    DEBUG = True
    
    ALLOWED_HOSTS = ["127.0.0.1", "localhost"]
    
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'DB',
            'USER': 'user',
            'PASSWORD': 'pass',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    
    
    STATIC_DIR = os.path.join(BASE_DIR, 'static')
    STATIC_URL = '/static/'
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]


Установить зависимости ::

    pip install -r req.txt
    
Создание БД и настройка CMS ::

    python manage.py deployOMS
    
Запустить dev сервер ::

    python manage.py runserver


Команды
--------
Запуск установщика ::

    oms-start
    
Создание файлов миграций ::

    python manage.py makemigrations
    
Применение миграций ::

    python manage.py migrate

Создание супер пользователя ::

    python manage.py createsuperuser



