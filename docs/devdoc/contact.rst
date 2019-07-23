Контакты
========
.. image:: ../_static/contact.png
   :scale: 50 %

.. image:: ../_static/contact_fields.png
.. image:: ../_static/contact_soc.png
Template tags
-------------

    Подключение тега. Если не указать шаблон, то будет взят по умолчанию.
    Если не указан name будут выбраны все записи контактов.

    .. code-block:: python

       {% load contact_tags %}

       {% contact %}

    Изменение шаблона

    .. code-block:: python

       {% contact name='Контакты', template='base/tags/contact/contact_block_tag.html' %}

    Шаблон для вывода полей контактов и соц. сетей.

    .. code-block:: python

        <p>{{ contact.name }}</p>
            '''Поля контактов'''
        {% for field in contact.get_contact_fields %}
            <p>
                {% if field.icon_ui %}
                        '''Иконка'''
                    <span class="{{ field.icon_ui }}"></span>
                {% elif field.icon %}
                        '''Загруженая иконка'''
                    <img src="{{ field.icon.image.url }}">
                {% endif %}
                    '''Поле 1'''
                {{ field.text|safe }}
                    '''Поле 2'''
                {{ field.text_two|safe }}
            </p>
        {% endfor %}
            '''Соц. ссылки'''
        {% for link_soc in contact.get_contact_socnet %}
            <p>
                <a href="{{ link_soc.get_link_contact_soc }}">
                    {% if link_soc.link.icon_ui %}
                            '''Иконка'''
                        <span class="{{ link_soc.link.icon_ui }}"></span>
                    {% elif link_soc.link.icon %}
                            '''Загруженая иконка'''
                        <img src="{{ link_soc.link.icon.image.url }}">
                    {% else %}
                           ''' Название, если нет иконок'''
                        {{ link_soc.link }}
                    {% endif %}
                </a>
            </p>
        {% endfor %}

Поля
----

Поля модели контактов
~~~~~~~~~~~~~~~~~~~~~~
    :name (max_length=100): Название
    :description (max_length=5000): Описание
    :map = (max_length=10000): Карта
    :slug (max_length=100, unique=True): URL

Поля контактов
~~~~~~~~~~~~~~~~~~~~~~
    :text (max_length=1000): Поле 1
    :text_two (max_length=1000): Поле 2
    :icon_ui (max_length=500): Класс иконки
    :icon (upload_to="icon/"): Иконка
    :contact ForeignKey: Связь с моделью Контакты

Поля соц. сети контактов
~~~~~~~~~~~~~~~~~~~~~~
    :contact_soc ForeignKey: Связь с моделью Контакты
    :your_id (max_length=100): Ваша ссылка
    :link ForeignKey: Связь с моделью Соц. сеть