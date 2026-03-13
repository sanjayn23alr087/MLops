FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# Run training to populate mlflow tracking (mlruns folder)
RUN python train.py

ENV PORT 8080
EXPOSE 8080

CMD ["python", "-m", "streamlit", "run", "app.py", "--server.port", "8080", "--server.address", "0.0.0.0"]
