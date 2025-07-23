> src\vehicle_price\train.py (
echo import joblib
echo from pathlib import Path
echo import pandas as pd
echo from sklearn.ensemble import RandomForestRegressor
echo from sklearn.pipeline import Pipeline
echo from sklearn.metrics import mean_absolute_error
echo.
echo from .config import load_config
echo from .data import load_raw_data
echo from .features import split_data, build_preprocessor
echo.
echo def train_main():
echo.    cfg = load_config()
echo.    df = load_raw_data()
echo.
echo.    train_df, test_df = split_data(df)
echo.    X_train = train_df[cfg["numeric_features"] + cfg["categorical_features"]]
echo.    y_train = train_df[cfg["target"]]
echo.
echo.    X_test = test_df[cfg["numeric_features"] + cfg["categorical_features"]]
echo.    y_test = test_df[cfg["target"]]
echo.
echo.    preprocessor = build_preprocessor()
echo.    model = RandomForestRegressor(n_estimators=100, random_state=42)
echo.
echo.    pipe = Pipeline([
echo.        ("preprocessor", preprocessor),
echo.        ("model", model)
echo.    ])
echo.
echo.    pipe.fit(X_train, y_train)
echo.
echo.    preds = pipe.predict(X_test)
echo.    mae = mean_absolute_error(y_test, preds)
echo.    print(f"Training complete. MAE: {mae:.2f}")
echo.
echo.    Path("models").mkdir(exist_ok=True)
echo.    joblib.dump(pipe, cfg["paths"]["model_file"])
echo.
echo if __name__ == "__main__":
echo.    train_main()
)
