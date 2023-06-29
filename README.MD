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
   docker-compose run web python backend/manage.py createsuperuser
   ```

### Эндпоинты
<a href="http://0.0.0.0:8000/docs/">Документация</a>


