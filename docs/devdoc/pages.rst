Страницы
=============
Это модуль статичных страниц.

Вывода страницы
---------------
Имя шаблона
    pages/index.html

.. code-block:: python

    {{ page.title }}
    {{ page.text|safe }}

Поля модели страницы
--------------------

    :title: Заголовок
    :text: Текст
    :edit_date: Дата редактирования
    :published_date: Дата публикации
    :published: Опубликовать или снять с публикации
    :template: Шаблон
    :slug: url

Template tags
--------------

get_block_page
~~~~~~~~~~~~~~
Вернет словарь с блоками страницы

.. code-block:: python

   {% load pages_tags %}
   {% get_block_page page as blockpage %}

   <h2>{{ blockpage.about.title }}</h2>
   <h3>{{ blockpage.about.sub_title }}</h3>
   <p>{{ blockpage.about.description|safe }}</p>

about - имя блока

page - объект страницы

get_list_block_page
~~~~~~~~~~~~~~~~~~~
Вывод списка блоков страниц

.. code-block:: python

   {% load pages_tags %}
   {% get_list_block_page page as blockpage %}
   {% for block in blockpage %}
        <div>
            <h2>{{ blockpage.about.title }}</h2>
            <h3>{{ blockpage.about.sub_title }}</h3>
            <p>{{ blockpage.about.description|safe }}</p>
        </div>
   {% endfor %}

about - имя блока

page - объект страницы