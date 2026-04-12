FROM python:3.11-slim

WORKDIR /app

# копіюємо requirements
COPY devops/requirements.txt .

# встановлюємо залежності
RUN pip install --no-cache-dir -r requirements.txt

# копіюємо весь код
COPY devops/ .

# порт (якщо API)
EXPOSE 8000

# команда запуску (зміни під свій проєкт)
CMD ["python", "main.py"]
