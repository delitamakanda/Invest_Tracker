#!/bin/bash

# Print debug information
echo "Current directory: $(pwd)"
echo "Contents of current directory:"
ls -la

# Read port information
cat /app/port_info.txt

# Determine the port to use
PORT="${PORT:-8080}"
echo "Using port: $PORT"

# Start Gunicorn
exec gunicorn backend.wsgi:application --bind 0.0.0.0:$PORT