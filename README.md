### Для запуска проекта:

#### Запуск контейнеров в фоновом режиме:
```
docker-compose up -d
```

#### Выполнить миграцию в контейнере c именем backend:
```
docker-compose run backend python manage.py migrate
```

#### Создание суперпользователя:
```
docker-compose run backend python manage.py createsuperuser
```

### Начало работы:

#### Регистрация нового пользователя:
```
http://localhost:8000/register/
```

#### Документация по API:
```
http://localhost:8000/api/docs/
```

#### Авторизация работает через JWT токен. Получить токен(1). Передать заголовок в запрос(2):
1. ```
   http://127.0.0.1:8000/api/v1/token/
   ```

2.```
{"Authorization": Bearer token}
```
