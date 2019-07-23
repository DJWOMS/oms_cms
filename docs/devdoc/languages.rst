Языки / Мультиязычность
=======================

Модуль для создания мультиязычного сайта.

Определить язык который выбрал пользователь можно забрав его из:
::

   request.session["lang"]

Template tags
--------------
Подключение тега. Если не указать шаблон, то будет взят по умолчанию.

.. code-block:: python

   {% load lang_tags %}

   {% list_lang %}

Изменение шаблона

.. code-block:: python

   {% list_lang template="lang.html" %}

Шаблон для выбора языков.

.. code-block:: python

    {% for lang in languages %}
        <ul>
            <li>
                <a href="{{ lang.get_absolute_url }}">{{ lang.name }}</a>
            </li>
        </ul>
    {% endfor %}

Поля модели языков
------------------

    :name: Название, отображается на сайте
    :slug: Сокращение названия, Пример: "ru"
    :is_default: Язык по умолчанию


