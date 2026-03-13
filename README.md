# 💻 LaptopAI: End-to-End MLOps Pipeline for Price Estimation

> **A robust MLOps project demonstrating model tracking, containerization, and interactive serving for laptop market valuation.**

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![MLflow](https://img.shields.io/badge/MLflow-Tracking-0194E2?style=for-the-badge&logo=mlflow&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Container-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

## 🌟 Project Overview

**LaptopAI** is an MLOps-centric application that predicts the market value of laptops based on core technical specifications. 

This project implements a complete lifecycle:
1.  **Data Generation & Training:** Automated training script with synthetic data generation.
2.  **Experiment Tracking:** Deep integration with **MLflow** to monitor model performance and versioning.
3.  **Interactive Deployment:** A premium **Streamlit** dashboard for real-time inference.
4.  **Containerization:** Fully dockerized for seamless deployment across any infrastructure (Local, Railway, AWS).

## 🚀 Key Features

*   **🔄 MLflow Lifecycle Tracking:** Logs every training run, capturing R² scores and MSE metrics automatically.
*   **🐳 Reproducible Environment:** Docker configuration ensures "it works on my machine" translates to "it works everywhere."
*   **📈 Dynamic Visualization:** Uses **Plotly** to visualize how different components (RAM, CPU, etc.) impact the final price.
*   **💎 Premium UI:** A modern, dark-themed dashboard with responsive elements and professional aesthetics.
*   **🤖 Random Forest Engine:** Utilizes an optimized Random Forest Regressor for reliable price estimations.

## 📊 MLOps Pipeline

The project follows a standard production-ready workflow:

| Component | Responsibility |
| :--- | :--- |
| **`train.py`** | Handles data ingestion, model training, and MLflow logging. |
| **`app.py`** | Serves the model via a high-performance Streamlit UI. |
| **`Dockerfile`** | Packages the entire environment into a lightweight image. |
| **MLflow Registry** | Houses the serialized model artifacts and performance metadata. |

## ⚙️ Installation & Setup

### 1. Setup Environment
Ensure you have Python 3.9+ installed. It is recommended to use a virtual environment.

```bash
# Install dependencies
pip install -r requirements.txt
```

### 2. Training the Model
Run the training script to generate the MLflow tracking data and model artifacts.
```bash
python train.py
```

### 3. Launch the Application
Start the Streamlit dashboard to interact with the model.
```bash
python -m streamlit run app.py
```

## 🐳 Running with Docker
To run the containerized version:
```bash
docker build -t laptop-ai-mlops .
docker run -p 8080:8080 laptop-ai-mlops
```

---
**Developed for MLOps Semester Project assignment**
