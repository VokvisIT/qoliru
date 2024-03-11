# Используем образ Node.js 14
FROM node:14

# Установка рабочей директории
WORKDIR /app

# Копирование зависимостей и установка их
COPY frontend/package*.json ./
RUN npm install

# Копирование остальных файлов приложения
COPY frontend .

# Команда для сборки Vue проекта
CMD ["npm", "run", "serve"]
