# Используем образ Python 3.11
FROM python:3.11

# Установка рабочей директории
WORKDIR /app

# Копирование зависимостей и установка их
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Копирование остальных файлов приложения
COPY . /app

# Выполнение миграций и запуск сервера
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
