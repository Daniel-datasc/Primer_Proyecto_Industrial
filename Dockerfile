FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

# Corregimos la línea para que sea un solo comando continuo
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "Scraper_proyecto.py"]
