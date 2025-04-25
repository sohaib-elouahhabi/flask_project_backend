# Project Documentation

## 1. How to Run

### 1.1 Create virtual environment (with Pipenv)

If you don't have **Pipenv** installed globally, you can install it with `pip`:

```bash
pip install pipenv
```

After installing Pipenv, follow these steps:

# Install the project dependencies and create a virtual environment

```bash
pipenv install
```

# Activate the virtual environment

```bash
pipenv shell
```

# Generate the migration script for the database

```bash
flask db migrate -m "Initial migration"
```

# Apply the migration and create the tables in the database

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
