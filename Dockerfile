FROM python:3.11-slim

WORKDIR /app

# Устанавливаем Poetry
RUN pip install poetry

# Копируем только файл с зависимостями
COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi --no-root --only main

COPY . .

EXPOSE 8000

# Основная команда, выполняемая после миграций
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


