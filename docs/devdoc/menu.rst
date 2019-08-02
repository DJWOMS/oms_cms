Меню
=====

Модуль для создания меню сайта из админ панели.


Template tags
--------------
menu_item
~~~~~~~~~~
Подключение тега. Если не указать шаблон, то будет взят по умолчанию.

menu
    Название вашего меню, обязательный аргумент

.. code-block:: python

   {% load menu_tags %}

   {% menu_item  menu="Тестовое" %}

Изменение шаблона

.. code-block:: python

   {% menu_item menu="Тестовое" template="menu.html" %}

Шаблон для вывода меню.

recursetree
    Template tag mptt для вывода подменю

.. code-block:: python

    {% load mptt_tags %}
    <ul>
        {% recursetree items %}
            <li>
                {% if node.url %}
                    <a class="" href="{{ node.url }}">{{ node.title }}</a>
                {% elif node.anchor %}
                    <a class="" href="{{ node.get_anchor }}">{{ node.title }}</a>
                {% else %}
                    <a class="" href="{{ node.content_object.get_absolute_url }}">{{ node.title }}</a>
                {% endif %}
                {% if not node.is_leaf_node %}
                    <ul class="children">
                        {{ children }}
                    </ul>
                {% endif %}
            </li>
        {% endrecursetree %}
    </ul>

for_menu_item
~~~~~~~~~~~~~~
Вывод списка пункот меню.

.. code-block:: python

    {% for_menu_item menu="Footer" as items %}
        <ul>
            {% for item in items %}
                <li>
                    {% if item.url %}
                        <a href="{{ item.url }}">{{ item.title }}</a>
                    {% elif item.anchor %}
                        <a href="{{ item.get_anchor }}">{{ item.title }}</a>
                    {% else %}
                        <a href="{{ item.content_object.get_absolute_url }}">{{ item.title }}</a>
                    {% endif %}
                </li>
            {% endfor %}
        </ul>

Поля
-----

Поля модели меню
~~~~~~~~~~~~~~~~
    :name (max_length=255): Название
    :status: Отображать только для зарегистрированных

Поля модели пунктов меню
~~~~~~~~~~~~~~~~~~~~~~~~~

    :title (max_length=255): Название пункта меню на сайте
    :name (max_length=255): Название латиницей
    :parent (related_name='children'): Родительский пункт
    :menu: Связь с моделью Меню
    :status: Отображать только для зарегистрированных
    :url: url на внешний ресурс
    :anchor: Якорь
    :content_type: Ссылка на любую модель
    :object_id: id записи из выбраной модель
    :content_object: content_object