Партнеры
========
Модуль для добавления ссылок на партнеров.

Template tags
-------------
Вывод списка всех партнеров

.. code-block:: python

    {% load partners_tags %}

    {% all_partners as partners %}
    {% for partner in partners %}
        <a href="{{ partner.link }}">
            {% if partner.picture %}
                <img src="{{ partner.picture.url }}">
            {% endif %}
        </a>
    {% endfor %}