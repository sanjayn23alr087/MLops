# house_price_mlops_production
# 🏠 RealEstateAI: Global House Price Predictor with MLOps.

> **A high-performance regression engine for California real estate, featuring multi-currency support and MLflow tracking.**

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![MLflow](https://img.shields.io/badge/MLflow-Tracking-0194E2?style=for-the-badge&logo=mlflow&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Container-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Railway](https://img.shields.io/badge/Deployment-Railway-0B0D0E?style=for-the-badge&logo=railway&logoColor=white)

## 🌟 Executive Summary

**RealEstateAI** is an advanced property valuation tool that leverages the **California Housing Dataset** to provide instant market estimates. 

Designed for the global market, this application allows users to toggle between multiple currencies (USD, INR, EUR, GBP) while maintaining a robust machine learning backend. By using **MLflow** for experiment versioning and **Docker** for standardized deployment, this project demonstrates a professional-grade MLOps workflow suitable for real-world real estate tech.

## 🚀 Key Features

* **🌍 Multi-Currency Support:** Real-time conversion logic allowing users to view property values in **INR (₹)**, **USD ($)**, **EUR (€)**, and **GBP (£)**.
* **📊 Feature Impact Analysis:** Interactive Plotly charts that visualize how Median Income, House Age, and Room Count affect the final price.
* **🔄 MLflow Lifecycle:** Every model training run is logged with its R² score and parameters, ensuring full transparency in the ML pipeline.
* **🐳 Containerized Logic:** Encapsulated in a **Docker** container to ensure consistent performance from local development to Railway cloud hosting.
* **📈 Dynamic UI:** A reactive **Streamlit** dashboard that updates prices and charts instantly based on user input.

## 🎤 Global Currency Guide

The system allows users to switch display modes via the sidebar. The underlying ML model predicts in USD, which is then dynamically converted:

| Currency | Symbol | Primary Use Case |
| :--- | :--- | :--- |
| **USD** | $ | Standard benchmark for California Real Estate. |
| **INR** | ₹ | Localized valuation for Indian investors. |
| **EUR** | € | European market compatibility. |
| **GBP** | £ | United Kingdom market compatibility. |

## 🛠️ System Architecture

The application follows a modular architecture optimized for CI/CD:
1.  **Training Engine (`train.py`):** Trains a Random Forest Regressor and registers the model in the **MLflow** database.
2.  **Conversion Engine:** A dynamic logic layer in `app.py` that handles international currency exchange math.
3.  **Cloud Layer:** Fully automated deployment on **Railway** using a custom **Dockerfile**.



## ScreenShot:

<img width="1919" height="1079" alt="RealEstate AI Screenshot" src="https://github.com/user-attachments/assets/your-new-screenshot-link" />


## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone [https://github.com/your-username/house_price_mlops_production.git](https://github.com/your-username/house_price_mlops_production.git)
cd house_price_mlops_production
```
### 2. Install Dependencies
```bash
pip install streamlit pandas numpy plotly mlflow scikit-learn
```
### 3. Running the Project

Follow these steps to initialize the MLOps environment:

Step 1: Train & Log Model
```bash
python train.py
```
Step 2: Launch Streamlit UI
```bash
streamlit run app.py
```
 By Vinothini K
