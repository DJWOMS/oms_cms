Галерея и фотографии
=======================

Модуль для создания галерей и вывода фотографий

Template tags
--------------

Список галерей
~~~~~~~~~~~~~~
Аргрументы для вывода галлереи:

name=имя галереи или pk=id галереи, без указания аргументов выведет все галереи.

.. code-block:: python

   {% load gallery_tags %}

   {% for_gallery as gallery%}

Список фотографий
~~~~~~~~~~~~~~~~~
Аргрументы для вывода фотографий:

gallery=None, без указания аргументов выведет все фото.

.. code-block:: python

   {% load gallery_tags %}

   {% for_photo gallery="Test" as photos %}
    {% for photo in photos %}
        <img src="{{ photo.image.url }}">
    {% endfor %}

Одна фотография
~~~~~~~~~~~~~~~~~
Аргрументы для вывода одной фотографии:

name=имя фото или pk=id фото, без указания аргументов вернет None.

.. code-block:: python

   {% load gallery_tags %}

   {% get_photo name="My photo" as photos %}