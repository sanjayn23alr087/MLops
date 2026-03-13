import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

def train_house_model():
    # Load Data
    data = fetch_california_housing()
    X = pd.DataFrame(data.data, columns=data.feature_names)
    y = data.target

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Set the experiment name explicitly (helps Railway stay organized)
    mlflow.set_experiment("House_Price_Experiment")

    with mlflow.start_run():
        model = RandomForestRegressor(n_estimators=100, max_depth=10)
        model.fit(X_train, y_train)

        # Log Metrics
        score = model.score(X_test, y_test)
        mlflow.log_metric("r2_score", score)
        mlflow.sklearn.log_model(model, "house_model")
        
        print(f"Model trained successfully. R2 Score: {score}")

if __name__ == "__main__":
    train_house_model()
