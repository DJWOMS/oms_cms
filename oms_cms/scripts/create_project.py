import os
import click
from django.conf import settings


@click.group()
def cli():
    pass


@cli.command()
@click.option('--name', prompt='Project name',
              help='project name')
@click.option('--project', prompt='Max or min project \n 0) Max \n 1) Min \n -> ',
              help='project', type=bool)
def cli_create(name, project):
    """Name project"""
    click.echo('Project name %s' % click.style(name, fg='green'))
    if project:
        pass
    else:
        os.system(f'django-admin startproject {name} --template=https://github.com/DJWOMS/oms_project/archive/master.zip')


@cli.command()
@click.option('--db', prompt='Max or min project \n 0) sqlite3 \n 1) postgresql \n 2) oracle \n 3) mysql \n-> ',
              help='data base', type=click.Choice(['0', '1', '2', '3']))
def data_base(db):
    """Выбор БД"""
    if db == '0':
        update_local_settings(db)
    else:
        option_db(db)


@cli.command()
@click.option('--name', prompt='Name DB', help='Name data base', type=str)
@click.option('--user', prompt='User DB', help='Name data base', type=str)
@click.option('--password', prompt='Password DB', help='Name data base', type=str)
@click.option('--host', prompt='Host DB', help='Name data base', type=str)
@click.option('--port', prompt='Port DB', help='Name data base', type=str)
def option_db(db, name, user, password, host, port):
    """Параметры базы данных"""
    update_local_settings(db, name, user, password, host, port)


def update_local_settings(db, name, user, password, host, port):
    """Изменение БД"""
    if db == '0':
        engine = 'django.db.backends.sqlite3',
        name = os.path.join(BASE_DIR, 'db.sqlite3'),
    elif db == '1':
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


# @cli.command()
# @click.option('--project', prompt='Max or min project \n 0) Max \n 1) Min \n -> ',
#               help='project', type=bool)
# def select_project(project):
#     """Create start project"""
#     click.echo('You %s!' % project)


if __name__ == '__main__':
    cli()