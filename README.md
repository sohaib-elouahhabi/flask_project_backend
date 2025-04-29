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

3. Running Tests
   3.1 Run Tests with Coverage
   To run the tests with coverage reporting, use the following command:

```bash
pipenv run pytest --cov=app --cov-config=.coveragerc tests/
coverage run -m pytest tests/

```

4. Update and Run the html in the browser

```bash
coverage html
htmlcov/index.html
```

5. Build Docker image and run database migration inside docker
   5.1
   change the variable localhost:5432 to db:5432
   SQLALCHEMY_DATABASE_URI='postgresql://postgres:1234@localhost:5432/flask_db'.
   Then run the commands below.

```bash
docker compose up --build
docker exec -it flask-app pipenv run flask db upgrade
```
