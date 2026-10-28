FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY Iris.csv .
COPY train_model.py .
COPY app.py .
COPY quality_gate.py .

RUN python train_model.py && python quality_gate.py

EXPOSE 5000

CMD ["python", "app.py"]
