FROM python:3.7-alpine

WORKDIR /www

COPY . .

# Use the built-in Python static server
CMD ["python", "-m", "http.server", "8000"]
