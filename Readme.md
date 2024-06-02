# Документация к проекту
## Введение
Данный проект состоит из фронтенд-приложения, построенного с помощью Vue 3, и бэкенд-приложения, построенного с помощью Django. Фронтенд- и бэкенд-приложения находятся в разных папках: frontend_two и backend соответственно.

## Предварительные требования
Перед началом работы убедитесь, что на вашей системе установлены следующие инструменты:
- Node.js (версия 14 или выше)
- Python (версия 3.7 или выше)
- pip (менеджер пакетов Python)
## Настройка фронтенда
Чтобы настроить фронтенд-приложение, выполните следующие действия:

Откройте окно терминала и перейдите в папку frontend_two.
Выполните следующую команду, чтобы установить необходимые зависимости:
```
npm install
npm run serve
```
Фронтенд-приложение будет доступно по адресу http://localhost:5173.
## Настройка бэкенда
Чтобы настроить бэкенд-приложение, выполните следующие действия:

Откройте новое окно терминала и перейдите в папку backend.
Создайте виртуальное окружение и активируйте его:
```
python -m venv venv
source venv/bin/activate
```
Выполните следующую команду, чтобы установить необходимые зависимости:
```
pip install -r requirements.txt
```
Выполните следующую команду, чтобы выполнить миграцию базы данных:
```
python manage.py migrate
```
Выполните следующую команду, чтобы запустить сервер разработки:
```
python manage.py runserver
```
Бэкенд-приложение будет доступно по адресу http://localhost:8000.
## Запуск приложения
Чтобы запустить приложение, убедитесь, что серверы фронтенда и бэкенда запущены. Откройте веб-браузер и перейдите по адресу http://localhost:8080.

Фронтенд-приложение будет взаимодействовать с бэкенд-приложением через API-конечные точки, определенные в файле backend/urls.py.
## Ссылки на модели
Ссылка на модели:https://drive.google.com/drive/folders/11xxqC-Fbhm0WZj3zLrSgEqIKeUSxfp-t?usp=sharing