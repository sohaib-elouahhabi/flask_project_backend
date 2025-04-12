### 1. Create virtual environment (with Pipenv)
```bash
pipenv install
pipenv shell
```

2. Create database migrations

```bash
flask db init
flask db migrate -m "Initial migration"
```

3. Apply migrations to the database

```bash
flask db upgrade
```

