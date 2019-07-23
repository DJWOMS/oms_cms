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




