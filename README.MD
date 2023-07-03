<a name="readme-test"></a>
<h1>Тестовое задание </h1>


### Как запустить
Из корня выполните команду
```sh
   docker-compose up --build
   ```

для повторного запуска можно использовать
   ```sh
   docker-compose up
   ```

### Создать суперпользователя
В корне директории
   ```sh
   docker-compose run web python manage.py createsuperuser
   ```

### Эндпоинты
<a href="http://0.0.0.0:8000/docs/">Документация</a> <br>
<a href="http://0.0.0.0:8000/api/v1/auth/users/">Создать пользователя</a> <br>
<a href="http://0.0.0.0:8000/api/v1/department/">Создать компанию</a> <br>
<a href="http://0.0.0.0:8000/api/v1/department/personal">Добавить сотрудника (POST method)</a> <br>
<a href="http://0.0.0.0:8000/api/v1/department/personal/{id}/">Удалить сотрудника (DELETE method)</a> <br>
<a href="http://0.0.0.0:8000/api/v1/personal/">Показать весь персонал (DELETE method)</a> <br>