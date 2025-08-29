# cw_habits_drf
HabitsApi — это API отслеживания привычек, интегрированный с Telegram. Основанный на «Атомных привычках» Джеймса Клира, он помогает вам сделать полезные привычки частью вашей жизни.

# Стек
Python 3.11, Django 5.2.3, PostgreSQL, Django REST Framework 3.16.0, DRF Simple JWT 5.5.0,
Celery 5.5.3, Redis 6.2.0, django-celery-beat 2.8.1, Pillow 11.2.1 

# Установка
1. Клонируйте репозиторий:

[https://github.com/MichaelMigachev/cw_habits_drf/tree/develop](https://github.com/MichaelMigachev/cw_habits_drf/tree/develop)

2. Установите зависимости проекта: poetry install
3. Создайте в корне проекта файл .env скопируйте в него переменные из файла .env.sample и заполните переменные своими данными
4. Запустите проект: python manage.py runserver

# Документация
после запуска проекта, документация будет доступна по адресам:

Swagger: http://localhost:8000/swagger/ 
Redoc: http://localhost:8000/redoc/


#### Чтобы начать рассылку напоминаний в терминале запустите celery worker командой

celery -A config worker -l INFO

#### Команда для windows:

celery -A config worker -l INFO -P eventlet


### Запуск через Docker Compose:

Для запуска всех сервисов выполните команду:

docker-compose up --build

Для запуска в фоновом режиме:

docker-compose up -d


После запуска доступность сервисов можно проверить командой:

docker-compose ps

### Деплой
В проекте настроен файл GitHub Actions workflow(.github/workflows/ci.yaml).
Благодаря этому при каждом push проекта запускается линтер flake8, запускаются тесты и проект деплоится на удалённый сервер после успешного прохождения тестов.
Для корректной работы необходимо настроить секреты в вашем репозитории в GitHub.
1. Создайте секреты:
CELERY_BROKER_URL,
CELERY_RESULT_BACKEND,
DEBUG,
POSTGRES_HOST,
DOCKER_HUB_ACCESS_TOKEN,
DOCKER_HUB_USER_NAME,
POSTGRES_DB,
POSTGRES_PASSWORD,
POSTGRES_USER,
POSTGRES_PORT,
SECRET_KEY,
SERVER_IP,
SSH_KEY,
SECRET_USER,
TELEGRAM_TOKEN
2. В сервисах 'app', 'celery', 'celery-beat' в строке image укажите свой DOCKER_HUB_USER_NAME

### Автор проекта Михаил Мигачев