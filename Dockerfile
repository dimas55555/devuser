FROM python:3.11-slim

WORKDIR /app

ARG AppVersion
ENV APP_VERSION=${AppVersion}

ENV PYTHONUNBUFFERED=1

COPY devops/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY devops/ .

EXPOSE 8000

CMD ["uvicorn", "main_orm:app", "--host", "0.0.0.0", "--port", "8000"]
