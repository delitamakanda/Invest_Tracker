FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY / .
COPY manage.py .

RUN python manage.py collectstatic --noinput || true

# Add this line to print debug information
RUN echo "PORT=${PORT:-8080}" > /app/port_info.txt

# Use a shell script to start the application
COPY start.sh /app/start.sh
RUN chmod +x /app/start.sh

CMD ["/app/start.sh"]