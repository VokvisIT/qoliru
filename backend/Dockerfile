# Используем образ Python 3.11
FROM python:3.11

# Установка рабочей директории
WORKDIR /app

# Копирование зависимостей и установка их
COPY backend/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Копирование остальных файлов приложения
COPY backend /app/

# Команда для запуска сервера Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]