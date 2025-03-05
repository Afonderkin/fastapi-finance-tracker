# justfile

set shell := ["powershell.exe", "-c"]

DC := "docker-compose"
STORE_FILE := "docker-composes/db.yaml"


# db
db-run:
    {{ DC }} -f {{ STORE_FILE }} up -d
db-stop:
    {{ DC }} -f {{ STORE_FILE }} down
db-logs:
    {{ DC }} -f {{ STORE_FILE }} logs -f
db-restart:
    {{ DC }} -f {{ STORE_FILE }} down
    {{ DC }} -f {{ STORE_FILE }} up -d

# alembic
makemigration message:
    cd src; alembic revision --autogenerate -m "{{ message }}"

migrate:
    cd src; alembic upgrade head

downgrade:
    cd src; alembic downgrade -1