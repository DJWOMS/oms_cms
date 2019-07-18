import os
import click


@click.command()
@click.argument('name')
def cli_create(name):
    """Create start project"""
    os.system(f'django-admin startproject {name} --template=https://github.com/DJWOMS/oms_project/archive/master.zip')