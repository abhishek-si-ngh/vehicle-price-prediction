import joblib
import pandas as pd
from config.config import load_config

def predict_main():
    cfg = load_config()

    # Sample input
    input_data = {
        "year": 2017,
        "mileage": 45000,
        "make": "Toyota",
        "model": "Corolla"
    }

    input_df = pd.DataFrame([input_data])

    # Load model
    model = joblib.load(cfg["paths"]["model_file"])

    # Predict
    prediction = model.predict(input_df)
    print(f"Predicted Price: ₹{prediction[0]:,.2f}")

if __name__ == "__main__":
    predict_main()
