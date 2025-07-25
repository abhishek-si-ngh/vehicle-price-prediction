import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from config.config import load_config


def split_data(df):
    cfg = load_config()
    return train_test_split(
        df,
        test_size=cfg["split"]["test_size"],
        random_state=cfg["split"]["random_state"]
    )


def build_preprocessor():
    cfg = load_config()
    numeric = cfg["numeric_features"]
    categorical = cfg["categorical_features"]

    num_pipe = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler())
    ])

    cat_pipe = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore"))
    ])

    return ColumnTransformer([
        ("num", num_pipe, numeric),
        ("cat", cat_pipe, categorical)
    ])
