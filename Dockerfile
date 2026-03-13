FROM python:3.9-slim

# Step 1: Install Git (Required by MLflow)
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Step 2: Copy and Install dependencies
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

# Step 3: Silence the MLflow Git warning and run training
ENV GIT_PYTHON_REFRESH=quiet
RUN python train.py

# Step 4: Web Server Setup
ENV PORT 8080
EXPOSE 8080

CMD ["streamlit", "run", "app.py", "--server.port", "8080", "--server.address", "0.0.0.0"]
