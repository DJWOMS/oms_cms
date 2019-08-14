Установка
=========

- Создать виртуальное окружение ::

    python -m venv venv

- Активировать виртуальное окружение

- Установить CMS ::

    pip install oms-cms

- Создать проект ::

    oms-start

Разработка
~~~~~~~~~~
- Сделать форк или клонировать репозиторий
- Создать файл oms_cms/config/local_settings.py и прописать конект к базе

.. code-block:: python

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

- Установить зависимости ::

    pip install -r req.txt

- Создание БД и настройка CMS ::

    python manage.py deployOMS

- Запустить dev сервер ::

    python manage.py runserver

Команды
~~~~~~~
Запуск установщика ::

    oms-start

Создание файлов миграций ::

    python manage.py makemigrations

Применение миграций ::

    python manage.py migrate

Создание супер пользователя ::

    python manage.py createsuperuser

Создание БД и настройка CMS ::

    python manage.py deployMin

Создание БД и настройка CMS с демо данными ::

    python manage.py deployOMS
