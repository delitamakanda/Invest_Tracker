FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY . /app

# Si requirements.txt est dans /app/backend/
RUN pip install --no-cache-dir -r requirements.txt

# collectstatic depuis le bon chemin
RUN python manage.py collectstatic --noinput

RUN mkdir -p /app/media
RUN mkdir -p /app/staticfiles
RUN ls -la staticfiles

CMD ["gunicorn", "backend.wsgi:application", "--bind", "0.0.0.0:8080", "--log-level=debug"]
