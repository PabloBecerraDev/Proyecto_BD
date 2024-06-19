
FROM python:3.10-slim

WORKDIR /app

COPY requirements/local.txt /app/requirements.txt

RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && pip install --no-cache-dir -r requirements.txt

COPY . /app

WORKDIR /app/mensajeria

EXPOSE 8000

CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
