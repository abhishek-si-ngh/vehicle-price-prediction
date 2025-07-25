import joblib
from pathlib import Path
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_absolute_error

from config.config import load_config
from data.data import load_raw_data
from src.vehicle_price.features import split_data, build_preprocessor


def train_main():
    cfg = load_config()
    df = load_raw_data()

    df = df.dropna(subset=[cfg["target"]])

    train_df, test_df = split_data(df)
    X_train = train_df[cfg["numeric_features"] + cfg["categorical_features"]]
    y_train = train_df[cfg["target"]]

    X_test = test_df[cfg["numeric_features"] + cfg["categorical_features"]]
    y_test = test_df[cfg["target"]]

    preprocessor = build_preprocessor()
    model = RandomForestRegressor(n_estimators=100, random_state=42)

    pipe = Pipeline([
        ("preprocessor", preprocessor),
        ("model", model)
    ])

    pipe.fit(X_train, y_train)

    preds = pipe.predict(X_test)
    mae = mean_absolute_error(y_test, preds)
    print(f"Training complete. MAE: {mae:.2f}")

    Path("models").mkdir(exist_ok=True)
    joblib.dump(pipe, cfg["paths"]["model_file"])

if __name__ == "__main__":
    train_main()
