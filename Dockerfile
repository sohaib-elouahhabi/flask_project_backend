FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY Pipfile Pipfile.lock /app/

RUN apt-get update && apt-get install -y \
    netcat-openbsd \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install pipenv && pipenv install --deploy --ignore-pipfile

COPY . /app/

EXPOSE 5000

CMD ["pipenv", "run", "gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "wsgi:app"]