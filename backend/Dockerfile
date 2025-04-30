FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY / .
COPY manage.py .

RUN python manage.py collectstatic --noinput || true

CMD gunicorn backend.wsgi:application --bind 0.0.0.0:${PORT:-8080}
