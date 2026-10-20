FROM python:3.11
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY scripts/bronze_layer_ingestion.py .
CMD ["python", "./scripts/bronze_layer_ingestion.py"]