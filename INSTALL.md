### Установка
- установить [poetry](https://python-poetry.org/docs/#installation)
```sh
curl -sSL https://install.python-poetry.org | python3 -
```
- в директории проекта выполнить:
```sh
poetry install
```
- в директории проекта выполнить:
```sh
make makemigrations
make migrate
```
- создать файл ".env", пример в ".env.example"
- изменить его внутри:
  - SECRET_KEY случайный набор символов, от длинной от 40
  - DEBUG режим запуска веб-приложния, True для тестирования и отладки, False для работы
