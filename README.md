# 💰 FastAPI Finance Tracker

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.13-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115.11-009688.svg)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-Supported-blue.svg)](https://www.docker.com/)

### 📌 Версия: `0.5.0 (MVP)`

**FastAPI Finance Tracker** — это приложение для **учёта финансов**, **анализа расходов** и **управления бюджетом**.

---

## 🛠️ **Стек технологий**
| Технология      | Версия  | Описание |
|----------------|---------|----------|
| 🐍 **Python**  | 3.13    | Язык программирования |
| ⚡ **FastAPI** | 0.115.11 | Веб-фреймворк |
| 🔥 **Uvicorn** | 0.34.0  | ASGI-сервер |
| 🗄️ **PostgreSQL** | 16 | База данных |
| 🏗️ **SQLAlchemy** | 2.0.38 | ORM |
| 🔄 **Alembic** | 1.15.1 | Миграции БД |
| 🐳 **Docker**  | latest  | Контейнеризация |
| 🎭 **Pytest**  | 8.1.1  | Тестирование |

---

## 🔥 **Планируемые функции**
* 🔔 Уведомления о превышении бюджета<br>
* 🌎 Поддержка мультивалютности<br>
* 📱 Мобильное приложение<br>
* 🚀 Кэширование данных (Redis / In-Memory Cache)<br>
* 🧪 Покрытие тестами (Pytest)<br>

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
