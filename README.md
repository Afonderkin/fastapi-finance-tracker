<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FastAPI Finance Tracker</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background: linear-gradient(135deg, #0b0f19, #0e1729);
            color: #d8ffe1;
            margin: 20px;
            padding: 20px;
            text-align: center;
        }
        h1 {
            font-size: 3em;
            font-weight: bold;
            color: #4cd964;
            text-shadow: 2px 2px 10px rgba(76, 217, 100, 0.5);
        }
        h2 {
            font-size: 2em;
            color: #38b44a;
            border-bottom: 2px solid #38b44a;
            display: inline-block;
            padding-bottom: 5px;
            margin-bottom: 20px;
        }
        .info-box {
            background: #121a2a;
            border-left: 5px solid #4cd964;
            padding: 15px;
            margin: 20px auto;
            width: 60%;
            text-align: left;
            border-radius: 8px;
        }
        .stack-container {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 15px;
            margin-top: 20px;
        }
        .stack-card {
            background: #121a2a;
            border: 1px solid rgba(76, 217, 100, 0.2);
            border-radius: 10px;
            padding: 15px;
            width: 160px;
            box-shadow: 0px 4px 10px rgba(76, 217, 100, 0.3);
            transition: transform 0.2s, box-shadow 0.2s;
            text-align: center;
        }
        .stack-card:hover {
            transform: translateY(-5px);
            box-shadow: 0px 6px 15px rgba(76, 217, 100, 0.5);
        }
        .stack-card img {
            height: 50px;
            margin-bottom: 10px;
        }
        .stack-card p {
            font-size: 1.1em;
            font-weight: bold;
            color: #d8ffe1;
            margin: 0;
        }
        pre {
            background: #1a2333;
            color: #d8ffe1;
            padding: 15px;
            border-radius: 8px;
            font-size: 1.1em;
            font-weight: bold;
            text-align: left;
            overflow-x: auto;
        }
        .command-section {
            text-align: left;
            max-width: 700px;
            margin: 0 auto;
        }
        .command-section h3 {
            font-size: 1.2em;
            color: #4cd964;
            margin-bottom: 8px;
            border-left: 4px solid #4cd964;
            padding-left: 10px;
        }
        .command-section pre {
            background: #0e1320;
            color: #d8ffe1;
            padding: 12px;
            border-radius: 6px;
            font-size: 1.1em;
            font-weight: bold;
            overflow-x: auto;
        }
    </style>
</head>
<body>
    <h1>💰 FastAPI Finance Tracker</h1>
    <h2>ℹ️ О проекте</h2>
    <div class="info-box">
        <p><strong>Версия:</strong> <span style="color: #4cd964;">0.5.0 (MVP)</span></p>
        <p><strong>Описание:</strong> Приложение для учёта финансов, анализа расходов и управления бюджетом.</p>
        <p><strong>Основные функции:</strong></p>
        <ul>
            <li>💰 Учёт доходов и расходов</li>
            <li>📊 Графики и аналитика</li>
            <li>⚡ Быстрый API на FastAPI</li>
            <li>📦 Хранение данных в PostgreSQL</li>
        </ul>
        <p><strong>Планируемые функции:</strong></p>
        <ul>
            <li>🔔 Уведомления о превышении бюджета</li>
            <li>🌎 Поддержка мультивалютности</li>
            <li>📱 Мобильное приложение</li>
            <li>🚀 <strong>Кэширование данных</strong> (Redis / In-Memory Cache для ускорения работы)</li>
            <li>🧪 <strong>Покрытие проекта тестами</strong> (Pytest для модульного тестирования)</li>
        </ul>
    </div>
    <h2>🛠️ Стек технологий</h2>
    <div class="stack-container">
        <div class="stack-card">
            <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" alt="Python">
            <p>Python 3.13</p>
        </div>
        <div class="stack-card">
            <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/fastapi/fastapi-original.svg" alt="FastAPI">
            <p>FastAPI 0.115.11</p>
        </div>
        <div class="stack-card">
            <img src="assets/uvicorn.svg" alt="Uvicorn">
            <p>Uvicorn 0.34.0</p>
        </div>
        <div class="stack-card">
            <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlalchemy/sqlalchemy-original.svg" alt="SQLAlchemy">
            <p>SQLAlchemy 2.0.38</p>
        </div>
        <div class="stack-card">
            <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg" alt="PostgreSQL">
            <p>AsyncPG 0.30.0</p>
        </div>
        <div class="stack-card">
            <img src="assets/alembic.svg" alt="Alembic">
            <p>Alembic 1.15.1</p>
        </div>
        <div class="stack-card">
            <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg" alt="Docker">
            <p>Docker (БД)</p>
        </div>
        <div class="stack-card">
            <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/poetry/poetry-original.svg" alt="Poetry">
            <p>Poetry</p>
        </div>
    </div>
    <h2>📦 Установка и запуск</h2>
    <div class="command-section">
        <h3>1️⃣ Клонирование репозитория</h3>
        <pre>git clone https://github.com/your-repo/fastapi-finance-tracker.git
cd fastapi-finance-tracker</pre>
        <h3>2️⃣ Установка зависимостей</h3>
        <pre>poetry install</pre>
        <h3>3️⃣ Установка Just (если не установлен)</h3>
        <pre># Для Linux/macOS:
cargo install just
# Для Windows:
# Скачать с GitHub: https://github.com/casey/just</pre>
        <h3>4️⃣ Запуск базы данных (Docker)</h3>
        <pre>just db-run</pre>
        <h3>5️⃣ Применение миграций</h3>
        <pre>just migrate</pre>
        <h3>6️⃣ Запуск приложения</h3>
        <pre>just app-run</pre>
    </div>
</body>
</html>
