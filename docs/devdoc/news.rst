Новости/Блог
============

Это модуль для ведение блога.

Категории
---------

Template tags
~~~~~~~~~~~~~

Подключение тега. Если не указать шаблон, то будет взят по умолчанию.

.. code-block:: python

   {% load news_tags %}

   {% category_list %}

Изменение шаблона

.. code-block:: python

   {% category_list template="categories.html" %}

Шаблон для вывода списка категорий.

.. code-block:: python

    <ul>
        {% for category in category_list %}
            <li>
                <a href="{{ category.get_absolute_url }}">{{ category.name }}</a>
            </li>
        {% endfor %}
    </ul>

Вывод списка всех категорий без использования шаблона.

.. code-block:: python

    {% load mptt_tags news_tags %}
    <ul>
        {% for_category_list as categories %}
        {% recursetree categories %}
            <li>
                <a href="{{ node.get_absolute_url }}">{{ node.name }}</a>
                {% if not node.is_leaf_node %}
                    <ul class="children">
                        {{ children }}
                    </ul>
                {% endif %}
            </li>
        {% endrecursetree %}
    </ul>

Поля модели категории
~~~~~~~~~~~~~~~~~~~~~
    :name: Название
    :lang: Язык
    :parent (related_name='children'): Родительская категория
    :template (default='news/post_list.html'): Шаблон
    :slug: url
    :published: Опубликовать или снять с публикации
    :paginated (default=5): Количество новостей на странице

Статьи/новости
----------------

Вывод списка статей
~~~~~~~~~~~~~~~~~~~
Имя шаблона
    news/post_list.html

.. code-block:: python

    {% for post in post_list %}
        {% if post.image %}
            <img src="{{ post.image.url }}">
        {% endif %}
        <p>{{ post.published_date }}</p>
        <p>
            {{ post.title }}
        </p>
    {% endfor %}

Вывод полной статьи
~~~~~~~~~~~~~~~~~~~
Имя шаблона
    news/post_detail.html

.. code-block:: python

    <h1>{{ post.title }}</h1>
    {% if post.author %}
        <p>{{ post.author }}</p>
    {% endif %}
    <p>Опубликовано {{ post.created_date }}</p>
    {% if post.image %}
        <img src="{{ post.image.url }}" alt="{{ post.title }}">
    {% endif %}
    {{ post.text|safe }}
    Просмотренно - {{ post.viewed }}

Поля модели статей
~~~~~~~~~~~~~~~~~~
    :author: Автор (FK)
    :title: Заголовок
    :subtitle: Под заголовок
    :mini_text: Краткое содержание статьи
    :text: Полное содержание статьи
    :created_date: Дата создания
    :edit_date: Дата редактирования
    :published_date: Дата публикации - когда будет опубликованно
    :image: "Главная фотография"
    :tag: Теги (M2M)
    :category: Категория (FK)
    :template: Шаблон
    :slug: url
    :published: Опубликовать или снять с публикации
    :viewed: Просмотров
    :status: Отображать для зарегистрированных пользователей или нет


Template tags
~~~~~~~~~~~~~

    Подключение тега. Если не указать шаблон, то будет взят по умолчанию.

    .. code-block:: python

       {% load news_tags %}

       {% post_list %}

    Изменение шаблона

    .. code-block:: python

       {% post_list template="news_block_tags.html" %}

    Шаблон для вывода списка статей.

    .. code-block:: python

        {% for post in post_list %}
            <h2><a href="{{ post.get_absolute_url }}"> {{ post.title }} </a></h2>
            {% if post.image %}
                <img src="{{ post.image.url }}">
            {% endif %}
            <p>{{ post.mini_text|safe }}</p>
            <p>{{ post.published_date }}</p>
        {% endfor %}

for_post_list
~~~~~~~~~~~~~~~~~~~~
Вывод списка статей без использования шаблона.

.. code-block:: python

    {% for_post_list as post_list %}
    {% for post in post_list %}
        <div>
            <h2><a href="{{ post.get_absolute_url }}">{{ post.title }}</a></h2>
            {% if post.image %}
                <img src="{{ post.image.url }}">
            {% endif %}
            <p>{{ post.mini_text|safe }}</p>
        </div>
    {% endfor %}

Теги
---------
for_tags_list
~~~~~~~~~~~~~
Вывод списка всег тегов статей.

.. code-block:: python

    {% load news_tags %}
    <ul>
        {% for_tags_list as tags %}
        {% for tag in tags %}
            <li><a href="{{ tag.get_absolute_url }}">{{ tag.name }}</a></li>
        {% endfor %}
    </ul>

Поля модели тегов
~~~~~~~~~~~~~~~~~~~~~
    :name: Имя
    :slug: url
    :published: Опубликовать или снять с публикации

Комментарии
-----------

Поля модели комментариев
~~~~~~~~~~~~~~~~~~~~~~~~

    :user ForeignKey: Связь с моделью Пользователей
    :post ForeignKey: Связь с моделью Новость
    :text (max_length=2000): Сообщение
    :date: Дата
    :update: Изменен
    :parent TreeForeignKey(related_name='children'): Родительский комментарий
    :published: Опубликовать или снять с публикации