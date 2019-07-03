# Use an OS debian
#FROM debian:latest

#RUN apt update && apt install -y
# pull official base image
FROM python:3.7.3

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /usr/src/oms_cms
#WORKDIR /app
COPY req.txt /
RUN pip install --upgrade pip
RUN pip install -r /req.txt
COPY . /usr/src/oms_cms
# install dependencies
#RUN pip install --upgrade pip
#RUN pip install pipenv
#COPY . /usr/src/oms_cms
#RUN pipenv install --skip-lock --system --dev

# copy project
#COPY . /usr/src/oms_cms/

#FROM python:3.7.2
#MAINTAINER DJWOMS <socanime@gmail.com>
#RUN apt install git
#ENV PYTHONUNBUFFERED 1
#RUN mkdir -p /home/root/oms_cms
#
#COPY oms_cms manage.py req.txt /home/root/oms_cms/
#WORKDIR /home/root/oms_cms
#RUN pip install git+https%3A%2F%2FDJWOMS%3AF00dz%21%405%40github.com%2FSGroupAM%2FMoses-CMS.git
#RUN django-admin startproject name --template=https://DJWOMS:F00dz!@5@github.com/SGroupAM/moses_project/archive/master.zip
#
##COPY . /opt/services/djangoapp/src
#RUN cd name && python manage.py collectstatic --no-input
#
#EXPOSE 8000
#CMD ["gunicorn", "-c", "config/gunicorn.conf.py", "--bind", ":8000", "--chdir", "config", "config.wsgi:application"]
