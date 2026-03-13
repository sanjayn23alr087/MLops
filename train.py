import mlflow
import mlflow.sklearn
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

def train_laptop_model():
    # 1. Generate Synthetic Data for Laptop Prices
    # RAM (4-64), Storage (128-2048), Screen (11-17), CPU (1.5-4.5)
    np.random.seed(42)
    n_samples = 500
    
    ram = np.random.choice([4, 8, 16, 32, 64], n_samples)
    storage = np.random.choice([128, 256, 512, 1024, 2048], n_samples)
    screen = np.random.uniform(11, 17.3, n_samples)
    cpu = np.random.uniform(1.8, 4.8, n_samples)
    
    # Simple price formula + noise
    price = (ram * 35) + (storage * 0.15) + (cpu * 150) + (screen * 20) + np.random.normal(0, 50, n_samples)
    
    df = pd.DataFrame({
        'RAM': ram,
        'Storage': storage,
        'ScreenSize': screen,
        'CPUSpeed': cpu,
        'Price': price
    })
    
    X = df.drop('Price', axis=1)
    y = df['Price']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 2. MLflow Experiment Tracking
    mlflow.set_experiment("Laptop_Price_Prediction")
    
    with mlflow.start_run():
        model = RandomForestRegressor(n_estimators=100, max_depth=10, random_state=42)
        model.fit(X_train, y_train)
        
        # Log Metrics
        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        
        mlflow.log_param("n_estimators", 100)
        mlflow.log_metric("mse", mse)
        mlflow.log_metric("r2_score", r2)
        mlflow.sklearn.log_model(model, "laptop_price_model")
        
        print(f"✅ Model trained. R2: {r2:.4f}, MSE: {mse:.2f}")

if __name__ == "__main__":
    train_laptop_model()
