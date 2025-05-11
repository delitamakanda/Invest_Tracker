FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH="/app/backend"

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY backend/ ./backend/
COPY manage.py .

RUN python manage.py collectstatic --noinput

RUN mkdir -p /app/media

RUN mkdir -p /app/staticfiles

RUN ls -la staticfiles

RUN python manage.py migrate

RUN python manage.py makesuperuser

CMD ["gunicorn", "backend.wsgi:application", "--bind", "0.0.0.0:8080", "--log-level=debug"]

