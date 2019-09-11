OMS CMS
=======
[![License](https://img.shields.io/pypi/l/oms-cms)](https://opensource.org/licenses/BSD-3-Clause)
[![Version](https://img.shields.io/pypi/v/oms-cms)](https://pypi.org/project/oms-cms/) 
[![Slack](https://img.shields.io/badge/Slack-chat-green)](https://join.slack.com/t/oms-cms/) 

[Documentation](https://oms-cms.readthedocs.io/ru/latest/)

* Python => 3.6
* Django => 2

OMS CMS is designed for a wide range of developers.

The system is open source, written using the Django framework in the Python programming language.

This CMS was designed by developers for a quick start and easy scalability.
OMS allows you to easily integrate with other django applications and use them immediately,
Or create new compatible applications!

This cms allows you to make a website in minutes.
You can use the basic template or download from the official site.

Modules
-------
* Pages
* News
   * Categories
   * Articles
   * Tags
* Comments
* Contacts
* Info block
* Languages, multilingualism
* Menu
* SEO
* Partners
* Search
* Links to social networks

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
    SECRET_KEY = 'b0!C@b!O_#Fdsf4#%#regdh@ana6l2$n=!P1ejm@'
    
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

__________________________________________________________

[Документация](https://oms-cms.readthedocs.io/ru/latest/)
 
* Python => 3.6
* Django => 2

OMS CMS создана для широкого круга разработчиков. 

Система имеет открытый исходный код, написана с использованием фреймворка Django на языке программирования Python. 

Данная CMS была задумана разработчиками для быстрого старта и легкой масштабируемости. 
OMS позволяет без трудностей интегрироваться с другими приложениями django и сразу же использовать их, 
либо создавать новые совместимые приложения!

Данная cms позволяет сделать сайт за считанные минуту. 
Вы можете использовать базовый шаблон или скачать с официального сайта.

Модули
------
* Страницы
* Новости
   * Категории
   * Статьи
   * Теги
* Комментарии
* Контакты
* Инфо блк
* Языки \ мультиязычность
* Меню
* SEO
* Партнеры
* Поиск
* Ссылки на социальные сети

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