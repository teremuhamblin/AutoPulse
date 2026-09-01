FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install fastapi uvicorn pyyaml
CMD ["uvicorn", "autopulse.api:app", "--host", "0.0.0.0", "--port", "8000"]
