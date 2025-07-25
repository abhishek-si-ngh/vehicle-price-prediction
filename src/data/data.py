import pandas as pd
from config.config import load_config

def load_raw_data():
    cfg = load_config()
    return pd.read_csv(cfg["paths"]["raw_data"])
