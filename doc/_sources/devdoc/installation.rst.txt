Установка
=========

- Создать виртуальное окружение ::

    python -m venv venv
- Активировать виртуальное окружение
- Установить CMS ::

    pip install git+https://github.com/DJWOMS/oms_cms.git
- Создать стартовый проект. В "name" указать имя вашего проекта ::

    oms-start "name"

Разработка
~~~~~~~~~~
- Сделать форк или клонировать репозиторий
- Создать файл oms_cms/config/local_settings.py и прописать конект к базе

.. code-block:: python

    import os
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
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

- Собрать статику ::

    python manage.py collectstatic

- Запустить dev сервер ::

    python manage.py runserver

Команды
~~~~~~~
Создание файлов миграций ::

    python manage.py makemigrations

Применение миграций ::

    python manage.py migrate

Создание супер пользователя ::

    python manage.py createsuperuser

Создание пользователей ::

    python manage.py adduser

Создание страниц ::

    python manage.py addpage

Создание тестовых постов и категории ::

    python manage.py addposts

Создание меню ::

    python manage.py addmenu

Выполнение всех команд разом ::

    python manage.py deploy

Выполнение всех команд разом и заполнить тест данными ::

    python manage.py deployOMS
