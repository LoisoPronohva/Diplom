# Используем официальный Python 3.12 образ
FROM python:3.12-slim

# Устанавливаем переменные окружения для корректной работы Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Создаем рабочую директорию внутри контейнера
WORKDIR /app

# Устанавливаем системные зависимости для psycopg2 и других пакетов
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Копируем только файл requirements.txt сначала (для кэширования слоев)
COPY requirements.txt .

# Устанавливаем зависимости проекта
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Копируем весь проект внутрь контейнера
COPY . .

# Создаем пользователя для запуска приложения (не root)
RUN useradd -m appuser
USER appuser

# Команда по умолчанию (используется в docker-compose.yml для web и celery)
# Для web контейнера: миграции + запуск сервера
# Для celery контейнера: будет переопределено командой в docker-compose.yml
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]