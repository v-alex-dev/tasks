# Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Installer les dépendances
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code de l'application
COPY . .

CMD ["gunicorn", "-b", "0.0.0.0:8000", "django_backend_app.wsgi:application"]
