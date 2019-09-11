Поиск
========
Модуль поиска.

Результат посика выводиться в шаблон search/search_list.html

get_search_form
---------------
Вывод формы посика

.. code-block:: python

    {% load search_tags %}
    <form action="{% url 'search:search' %}" method="get">
        {% get_search_form as form %}
        {{ form }}
         <button type="submit">Поиск</button>
    </form>