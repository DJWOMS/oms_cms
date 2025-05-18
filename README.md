# OMS CMS

[![Build Status](https://travis-ci.org/DJWOMS/oms_cms.svg?branch=master)](https://travis-ci.org/DJWOMS/oms_cms)
[![Coverage Status](https://coveralls.io/repos/github/DJWOMS/oms_cms/badge.svg?branch=master)](https://coveralls.io/github/DJWOMS/oms_cms?branch=master)
[![License](https://img.shields.io/pypi/l/oms-cms)](https://opensource.org/licenses/BSD-3-Clause)
[![Version](https://img.shields.io/pypi/v/oms-cms)](https://pypi.org/project/oms-cms/)
[![Python](https://img.shields.io/badge/python-3.7%2B-blue)](https://www.python.org/)
[![Django](https://img.shields.io/badge/django-3.0%2B-green)](https://www.djangoproject.com/)
[![Documentation](https://img.shields.io/badge/docs-latest-brightgreen)](https://oms-cms.readthedocs.io/ru/latest/)

Высокоуровневая open-source CMS на Python/Django для быстрого старта и масштабируемых сайтов.

## Основные возможности

- 🚀 Быстрый старт и легкая масштабируемость
- 🔌 Простая интеграция с другими Django-приложениями
- 🌐 Мультиязычность из коробки
- 📱 Адаптивный дизайн
- 🔍 Встроенный поиск
- 📊 SEO-оптимизация
- 🔐 Безопасность и производительность

## Модули

- 📄 Страницы
- 📰 Новости (категории, статьи, теги)
- 💬 Комментарии
- 📞 Контакты
- ℹ️ Инфоблоки
- 🌍 Языки и мультиязычность
- 📑 Меню
- 🔍 SEO
- 🤝 Партнеры
- 🔎 Поиск
- 🔗 Социальные сети
- 📱 OpenGraph

## Требования

- Python 3.7+
- Django 3.0+
- PostgreSQL/SQLite/MySQL/Oracle
- Node.js 14+ (для frontend)

## Установка

1. Создайте виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# или
.\venv\Scripts\activate  # Windows
```

2. Установите CMS:
```bash
pip install oms-cms
```

3. Создайте проект:
```bash
oms-start
```

## Быстрый старт с Docker

1. Клонируйте репозиторий:
```bash
git clone https://github.com/DJWOMS/oms_cms.git
cd oms_cms
```

2. Запустите с Docker Compose:
```bash
docker-compose up -d
```

## Структура проекта

```
.
├── oms_cms/           # Исходный код CMS
│   ├── backend/       # Модули (pages, news, comments, ...)
│   ├── config/        # Настройки (settings.py, local_settings.py)
│   ├── scripts/       # CLI-утилиты
│   ├── static/        # Статика
│   └── templates/     # Шаблоны
├── manage.py          # Django entrypoint
├── requirements/      # Зависимости
│   ├── base.txt      # Основные зависимости
│   ├── dev.txt       # Зависимости для разработки
│   └── prod.txt      # Зависимости для продакшена
├── setup.py          # Установка как пакета
└── docs/             # Документация
```

## Переменные окружения

Создайте файл `.env` на основе `.env.example`:

```bash
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=postgres://user:password@localhost:5432/omsCMS
```

## Запуск

1. Примените миграции:
```bash
python manage.py migrate
```

2. Создайте суперпользователя:
```bash
python manage.py createsuperuser
```

3. Запустите сервер:
```bash
python manage.py runserver
```

## Тестирование

```bash
# Запуск тестов
python manage.py test

# Запуск тестов с покрытием
coverage run manage.py test
coverage report
```

## Документация

- [Руководство пользователя](https://oms-cms.readthedocs.io/ru/latest/)
- [API документация](https://oms-cms.readthedocs.io/ru/latest/api.html)
- [Руководство разработчика](https://oms-cms.readthedocs.io/ru/latest/dev.html)

## Внесение вклада

Мы приветствуем вклад в развитие проекта! Пожалуйста, ознакомьтесь с [CONTRIBUTING.md](CONTRIBUTING.md) для получения дополнительной информации.

## Лицензия

Проект распространяется под лицензией BSD. Подробности в файле [LICENSE](LICENSE).

## Поддержка

- [Документация](https://oms-cms.readthedocs.io/ru/latest/)
- [Issues](https://github.com/DJWOMS/oms_cms/issues)
- [Slack](https://join.slack.com/t/oms-cms/)

## Сборка пакета

### Локальная сборка

1. Установите инструменты сборки:
```bash
pip install build twine
```

2. Соберите пакет:
```bash
python -m build
```

3. Проверьте собранный пакет:
```bash
twine check dist/*
```

4. Установите пакет локально:
```bash
pip install dist/oms_cms-0.11.0.tar.gz
```

### Публикация в PyPI

1. Создайте аккаунт на [PyPI](https://pypi.org)

2. Создайте файл `~/.pypirc`:
```ini
[pypi]
username = your_username
password = your_password
```

3. Загрузите пакет:
```bash
twine upload dist/*
```

### Разработка

Для разработки установите пакет в режиме разработки:
```bash
pip install -e .
```

Или с дополнительными зависимостями:
```bash
pip install -e ".[dev]"  # для разработки
pip install -e ".[prod]"  # для продакшена
```
