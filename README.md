# Digests Searcher

## Отписание

**«Digests FastAPI»** - микросервис, который формирует дайджесты контента
для пользователей на основе их подписок. Дайджест представляет собой выборку
постов из различных источников, на которые подписан пользователь.

### Функионал

1. Получение запроса на формирование дайджеста: Микросервис принимаeт запрос от
   основного приложения на формирование дайджеста для
   пользователя, идентифицируемого по уникальному ID.

2. Определение подписок пользователя: После получения запроса, микросервис
   должен определяет источники, на которые подписан пользователь, используя
   информацию о подписках пользователя.

3. Сбор постов из подписок: Зная подписки пользователя, микросервис
   собираeт посты из этих источников.

4. Фильтрация постов: Собранные посты фильтруются по рейтингу

5. Создание дайджеста: После фильтрации, оставшиеся посты упаковываются в
   дайджест. Дайджест - это совокупность постов, отобранных для пользователя.

6. Отправка дайджеста: Сформированный дайджест возвращается в главное
   приложение, которое предоставит его пользователю.

# Технологии

- [Python 3.10](https://www.python.org/downloads/release/python-388/)
- [Fastapi 0.100.0](https://fastapi.tiangolo.com/)
- [Pydantic](https://docs.pydantic.dev/latest/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [PostgreSQL 13.0](https://www.postgresql.org/download/)
- [gunicorn 20.0.4](https://pypi.org/project/gunicorn/)
- [nginx 1.19.3](https://nginx.org/ru/download.html)
- # Контейнер

- [Docker 20.10.14](https://www.docker.com/)
- [Docker Compose 2.4.1](https://docs.docker.com/compose/)

# URL's

- http://localhost:8000/users/1/digest
- # Локальная установка

Клонируйте репозиторий и перейдите в него в командной строке:

```sh
git clone https://github.com/kvazymir1199/digests_searcher.git && cd digests_searcher
```

Создайте .env файл командой:

```sh
touch .env
```

и заполните его данными:

```sh
#.env
DB_NAME=<db>
DB_USER=<postgres>
DB_PASSWORD=<12345>
```

Выполните команду

```sh
docker-compose up -d
```

Для заполнения базы тестовыми данными воспользуйтесь командой

```sh
docker-compose exec app python fill_db.py
```

**GET**: http://127.0.0.1:8000/api/users/
Пример ответа:

```json
{
  "posts": [
    {
      "content": "Bitcoin now lose"
    },
    {
      "content": "WOW"
    },
    {
      "content": "USD now lower than EUR"
    },
    {
      "content": "Waterfall in Alanya"
    },
    {
      "content": "Turkey give 100000 USD for rebuilding Waterfalls"
    }
  ]
}
```

Для фильтрации по рейтингу используйте query_params в запросе
**GET**: http://127.0.0.1:8000/api/users/1/digest?rating=9
Пример ответа:

```json
{
  "posts": [
    {
      "content": "Bitcoin now lose"
    }
  ]
}
```

## Автор:

* [kvazymir1199](https://github.com/kvazymir1199)