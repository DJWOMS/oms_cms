import os
import click


@click.group()
def cli():
    pass


@cli.command()
@click.option('--name', prompt='Project name', help='project name')
@click.option('--project', prompt='Add templates \n 0) No \n 1) Yes \n -> ', help='project', type=bool)
@click.option('--db', prompt='Select your database \n 0) sqlite3 \n 1) postgresql \n 2) oracle \n 3) mysql \n-> ',
              help='data base', type=click.Choice(['0', '1', '2', '3']))
def cli_create(name, project, db):
    """Name project"""
    click.echo('Project name %s' % click.style(name, fg='green'))
    if project:
        os.system(
            f'django-admin startproject {name} --template=https://github.com/DJWOMS/oms_project/archive/master.zip')
    else:
        os.system(
            f'django-admin startproject {name} --template=https://github.com/DJWOMS/oms_project_min/archive/master.zip')

    if db == '0':
        update_local_settings(db, name)
    else:
        option_db((db, name))


@cli.command()
@click.argument("db", nargs=-1)
@click.option('--name', prompt='Name DB', help='Name data base', type=str)
@click.option('--user', prompt='User DB', help='Name data base', type=str)
@click.option('--password', prompt='Password DB', help='Name data base', type=str)
@click.option('--host', prompt='Host DB', help='Name data base', default="localhost", type=str)
@click.option('--port', prompt='Port DB', help='Name data base', default="5432", type=str)
def option_db(db, name, user, password, host, port):
    """Параметры базы данных"""
    database, pr_name = db
    update_local_settings(database, pr_name, name, user, password, host, port)


def update_local_settings(db, pr_name, name=None, user=None, password=None, host=None, port=None):
    """Изменение БД"""
    dirs = os.path.join(os.path.dirname(os.path.abspath(f"{pr_name}")), pr_name)
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
        file_read = open("{}/config/local_settings.py".format(dirs), "r")
        file = file_read.read()
        file_read.close()
        line = file.replace("DATABASES = ", "DATABASES = {} \n#".format(DATABASES))
        file = open("{}/config/local_settings.py".format(dirs), "w")
        file.write(line)
        file.close()
    select_lang((pr_name,))


@cli.command()
@click.argument("pr_name", nargs=-1)
@click.option('--lang', prompt='Language admin (en, ru) \n -> ', default="ru", help='Language admin', type=str)
def select_lang(pr_name, lang):
    """Select language admin"""
    dirs = os.path.join(os.path.dirname(os.path.abspath(f"{pr_name[0]}")), pr_name[0])
    langs = {
        "en": ('en', 'English'),
        "ru": ('ru', 'Russian'),
    }
    file_read = open("{}/config/settings.py".format(dirs), "r")
    file = file_read.read()
    file_read.close()
    line = file.replace("LANGUAGE_CODE = 'en'", "LANGUAGE_CODE = '{}'".format(lang))
    line = line.replace("LANGUAGES = ()", "LANGUAGES = ({},)".format(langs[lang]))
    file = open("{}/config/settings.py".format(dirs), "w")
    file.write(line)
    file.close()

    select_demo(pr_name)


@cli.command()
@click.argument("pr_name", nargs=-1)
@click.option('--demo', prompt='Add demo data \n 0) No \n 1) Yes \n-> ', help='Language admin', type=bool)
def select_demo(pr_name, demo):
    """Select database demo"""
    dirs = os.path.join(os.path.dirname(os.path.abspath(f"{pr_name[0]}")), pr_name[0])
    if demo:
        os.system(f'python {dirs}/manage.py deployOMS')
    else:
        os.system(f'python {dirs}/manage.py deployMin')
    add_user(pr_name)


@cli.command()
@click.argument("pr_name", nargs=-1)
@click.option('--user', prompt='Create superuser \n 0) No \n 1) Yes \n-> ', help='', type=bool)
def add_user(pr_name, user):
    """Create superuser"""
    dirs = os.path.join(os.path.dirname(os.path.abspath(f"{pr_name[0]}")), pr_name[0])
    if user:
        os.system(f'python {dirs}/manage.py createsuperuser')


if __name__ == '__main__':
    cli()