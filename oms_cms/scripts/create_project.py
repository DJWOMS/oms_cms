import os
import click

import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()
from django.conf import settings


@click.group()
def cli():
    pass
# cli = click.Group()


@cli.command()
@click.option('--name', prompt='Project name',
              help='project name')
@click.option('--project', prompt='Max or min project \n 0) Max \n 1) Min \n -> ',
              help='project', type=bool)
@click.option('--db', prompt='Select your database \n 0) sqlite3 \n 1) postgresql \n 2) oracle \n 3) mysql \n-> ',
              help='data base', type=click.Choice(['0', '1', '2', '3']))
def cli_create(name, project, db):
    """Name project"""
    click.echo('Project name %s' % click.style(name, fg='green'))

    if project:
        pass
    else:
        os.system(f'django-admin startproject {name} --template=https://github.com/DJWOMS/oms_project/archive/master.zip')
    if db == '0':
        update_local_settings(db)
    else:
        option_db(db)


@cli.command()
@click.argument("db")
@click.option('--name', prompt='Name DB', help='Name data base', type=str)
@click.option('--user', prompt='User DB', help='Name data base', type=str)
@click.option('--password', prompt='Password DB', help='Name data base', type=str)
@click.option('--host', prompt='Host DB', help='Name data base', type=str)
@click.option('--port', prompt='Port DB', help='Name data base', type=str)
def option_db(db, name, user, password, host, port):
    """Параметры базы данных"""
    update_local_settings(db, name, user, password, host, port)


def update_local_settings(db, name=None, user=None, password=None, host=None, port=None):
    """Изменение БД"""
    if db != '0':
        if db == '1':
            engine = 'django.db.backends.postgresql_psycopg2'
            port = '5432'
        elif db == '2':
            engine = 'django.db.backends.oracle'
            port = '1540'
        elif db == '3':
            engine = 'django.db.backends.mysql'

        DATABASES = {
            'default': {
                'ENGINE': engine,
                'NAME': name,
                'USER': user,
                'PASSWORD': password,
                'HOST': host,
                'PORT': port,
            }
        }


        file_read = open("{}/config/local_settings.py".format(settings.BASE_DIR), "r")
        file = file_read.read()
        file_read.close()
        line = file.replace("DATABASES = {}".format(DATABASES))
        file = open("/config/local_settings.py".format(settings.BASE_DIR), "w")
        file.write(line)
        file.close()
    select_lang()


@cli.command()
@click.option('--lang', prompt='Language admin (en-us, ru-ru) -> ',
              help='Language admin', type=str)
def select_lang(lang):
    """Select language admin"""
    file_read = open("{}/config/local_settings.py".format(settings.BASE_DIR), "r")
    file = file_read.read()
    file_read.close()
    line = file.replace("LANGUAGE_CODE = '{}'".format(lang))
    file = open("/config/local_settings.py".format(settings.BASE_DIR), "w")
    file.write(line)
    file.close()

    select_demo()


@cli.command()
@click.option('--demo', prompt='Add demo data \n 0) Yes \n 1) No \n -> -> ',
              help='Language admin', type=bool)
def select_demo(demo):
    """Select database demo"""
    if demo == '0':
        os.system(f'python manage.py deployOMS')
    else:
        os.system(f'python manage.py deployMin')


if __name__ == '__main__':
    cli()