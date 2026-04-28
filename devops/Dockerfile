FROM python:3.11-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1

COPY devops/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY devops/ .

CMD ["python", "migration_job/main.py"]
