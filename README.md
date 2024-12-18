## Описание проекта

Это Django-приложение для управления заказами на роботов. Когда робот появляется в наличии, система отправляет уведомление клиенту, сделавшему заказ.

## Автор

Бондаренко Алексей Олегович
- Telegram: [@alovsemprivet](https://t.me/alovsemprivet)
- GitHub: [Pr1ority](https://github.com/Pr1ority)

## Технологический стек

- Backend: Django
- Database: Sqlite3
- Язык программирования: Python 3

## Как развернуть репозиторий на сервере

1. Клонируйте репозиторий
```bash
git clone https://github.com/Pr1ority/R4C.git
```
2. Перейдите в корневую директорию
```bash
cd R4C
```
3. Настройте виртуальное окружение
```bash
python -m venv venv
```
Для macOS/Linux
```bash
source venv/bin/activate
```
Для Windows
```bash
source venv/Scripts/activate
```
```bash
pip install -r requirements.txt
```
4. Заполните .env
Пример:
```example.env
SECRET_KEY=your_secret_key
```
5. Подготовьте базу данных

```bash
python manage.py migrate
```
```bash
python manage.py createsuperuser
```
6. Запустите сервер
```bash
python manage.py runserver
```

## Использование
1. Вход в админку
Перейдите по адресу http://127.0.0.1:8000/admin и войдите с помощью учётных данных суперпользователя.

2. Создание заказов
В разделе "Orders" создайте заказ, указав клиента и серийный номер робота.

3. Добавление робота в наличии
В разделе "Robots" создайте робота с указанным серийным номером.
Система автоматически отправит уведомление клиенту.

4. Проверка отправки писем
Письма будут выводиться в консоль, так как используется тестовый почтовый бэкенд.

## Пример с cURL

Чтобы создать запись о роботе:

```bash
curl -X POST http://127.0.0.1:8000/robots/add-robot/ \
-H "Content-Type: application/json" \
-d '{"model":"R2","version":"D2","created":"2024-12-18 16:59:59"}'
```

## Сводка производства роботов

Скачать сводку производства роботов за последнюю неделю можно по адресу http://127.0.0.1:8000/robots/weekly-summary/