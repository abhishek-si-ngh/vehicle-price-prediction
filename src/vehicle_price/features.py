cd C:\Projects\vehicle-price-prediction

> src\vehicle_price\features.py (
echo import pandas as pd
echo from sklearn.model_selection import train_test_split
echo from sklearn.preprocessing import OneHotEncoder
echo from sklearn.compose import ColumnTransformer
echo from sklearn.pipeline import Pipeline
echo from sklearn.impute import SimpleImputer
echo from sklearn.preprocessing import StandardScaler
echo from .config import load_config
echo.
echo def split_data(df):
echo.    cfg = load_config()
echo.    return train_test_split(
echo.        df,
echo.        test_size=cfg["split"]["test_size"],
echo.        random_state=cfg["split"]["random_state"]
echo.    )
echo.
echo def build_preprocessor():
echo.    cfg = load_config()
echo.    numeric = cfg["numeric_features"]
echo.    categorical = cfg["categorical_features"]
echo.
echo.    num_pipe = Pipeline([
echo.        ("imputer", SimpleImputer(strategy="median")),
echo.        ("scaler", StandardScaler())
echo.    ])
echo.
echo.    cat_pipe = Pipeline([
echo.        ("imputer", SimpleImputer(strategy="most_frequent")),
echo.        ("encoder", OneHotEncoder(handle_unknown="ignore"))
echo.    ])
echo.
echo.    return ColumnTransformer([
echo.        ("num", num_pipe, numeric),
echo.        ("cat", cat_pipe, categorical)
echo.    ])
)
