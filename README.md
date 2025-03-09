# 💰 FastAPI Finance Tracker

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.13-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115.11-009688.svg)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-Supported-blue.svg)](https://www.docker.com/)

## ℹ️ О проекте

### 📌 Версия: `0.5.0 (MVP)`

**FastAPI Finance Tracker** — это приложение для **учёта финансов**, **анализа расходов** и **управления бюджетом**.

### 🔹 Основные функции:
- 💰 **Учёт доходов и расходов**
- 📊 **Графики и аналитика**
- ⚡ **Быстрый API на FastAPI**
- 📦 **Хранение данных в PostgreSQL**

### 🔥 Планируемые функции:
- 🔔 **Уведомления о превышении бюджета**
- 🌎 **Поддержка мультивалютности**
- 📱 **Мобильное приложение**
- 🚀 **Кэширование данных** (Redis / In-Memory Cache для ускорения работы)
- 🧪 **Покрытие проекта тестами** (Pytest для модульного тестирования)
- 🔑 **Аутентификация и управление пользователями**
  
---

## 🛠️ Стек технологий

| Технология   | Иконка  | Версия  | Описание |
|-------------|--------|---------|----------|
| Python      | ![Python](https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg) | 3.13 | Язык программирования |
| FastAPI     | ![FastAPI](https://cdn.jsdelivr.net/gh/devicons/devicon/icons/fastapi/fastapi-original.svg) | 0.115.11 | Веб-фреймворк |
| Uvicorn     | ![Uvicorn](assets/uvicorn.svg) | 0.34.0 | ASGI-сервер |
| PostgreSQL  | ![PostgreSQL](https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg) | 16 | База данных |
| SQLAlchemy  | ![SQLAlchemy](https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlalchemy/sqlalchemy-original.svg) | 2.0.38 | ORM |
| Alembic     | ![Alembic](assets/alembic.svg) | 1.15.1 | Миграции БД |
| Docker      | ![Docker](https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg) | latest | Контейнеризация |
| Pytest      | 🧪 | 8.1.1 | Тестирование |

---

## 🚀 **Установка и запуск**
### 🔹 **1. Клонирование репозитория**
```sh
git clone https://github.com/your-repo/fastapi-finance-tracker.git
cd fastapi-finance-tracker
```

### 🔹 **2. Установка зависимостей**
```sh
poetry install
```

### 🔹 **3. Установка Just (если не установлен)**
```sh
# Для Linux/macOS:
cargo install just

# Для Windows:
# Скачать с GitHub: https://github.com/casey/just
```

### 🔹 **4. Запуск базы данных (Docker)**
```sh
just db-run
```

### 🔹 **5. Применение миграций**
```sh
just migrate
```

### 🔹 **6. Запуск приложения**
```sh
just app-run
```

---

## 📜 **Лицензия**
Проект распространяется под лицензией MIT.<br>
Полный текст лицензии доступен в файле LICENSE.
