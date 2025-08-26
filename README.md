Описание проекта

Это проект RESTful API для управления товарами в интернет-магазине, реализованный с использованием фреймворка FastAPI и SQLAlchemy ORM. 
Основная цель — предоставление простого и эффективного способа создавать, просматривать и управлять товарами, учитывая права доступа пользователей.

Основные возможности

- Добавление новых товаров
- Просмотр списка всех доступных товаров
- Поиск товаров по категориям и подкатегориям
- Детальная информация о каждом товаре
- Авторизация и проверка ролей пользователей



Структура репозитория


project/
│   README.md
│   main.py       # Запуск приложения
│   
├───app           # Директория приложений
│   ├───backend     # Базовые модули backend
│   │   └───db_depends.py  # Dependency injection для подключения к базе данных
│   │   
│   ├───models      # Модель данных
│   │   └───__init__.py    
│   │   
│   ├───routers     # Маршруты API
│   │   ├───auth.py     # Аутентификация и авторизация
│   │   └───products.py # Продукты
│   │   
│   └───schemas     # Пирамиды моделей данных (Pydantic)
│       └───__init__.py    
│       
└───tests          # Директория тестов
    └───test_products.py


Установка и запуск

Предварительные требования

- Python >= 3.8
- PostgreSQL
- pipenv (рекомендуется для виртуального окружения)

Настройка среды

1. Клонируйте репозиторий:
git clone https://github.com/yourusername/WillyShpilly/FastAPIREST.git
cd product-management-api

2. Установите зависимости:
pip install -r requirements.txt

3. Создайте файл .env и заполните необходимые переменные окружения:
DATABASE_URL="postgresql+asyncpg://user:password@localhost/dbname"
SECRET_KEY="your-secret-key-here"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30

4. Примените миграции базы данных (если используете Alembic):
alembic upgrade head

5. Запустите приложение:
uvicorn main:app --reload













