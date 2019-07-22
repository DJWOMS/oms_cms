Новости/Блог
============

Это модуль для ведение блога

Вывод списка статей
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    {% for post in post_list %}
        {% if post.image %}
            <img src="{{ post.image.url }}">
        {% endif %}
        <p class="">{{ post.published_date }}</p>
        <p class="">
            {{ post.title }}
        </p>
    {% endfor %}

Поля модели статей
------------------
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
    :published: Опубликовать?
    :viewed: Просмотров
    :status: Отображать для зарегистрированных


Template tags
~~~~~~~~~~~~~