# 🚗 Vehicle Price Prediction App

This project is a **Machine Learning web app** that predicts the price of a used vehicle based on inputs like **Make**, **Model**, **Year**, and **Mileage**. It's built with `scikit-learn`, `Streamlit`, and deployed on **Render** for public use.

---

## 🔍 Features

- ML-powered vehicle price prediction using `RandomForestRegressor`
- Interactive UI built with **Streamlit**
- Dynamic dropdowns for Make & filtered Model options
- Input: Year, Mileage, Make, Model
- Output: Predicted resale price
- Deployed online — accessible on any device!

---

## 🧠 Tech Stack

- **Frontend & Deployment**: Streamlit, Render
- **Backend ML**: scikit-learn, pandas, joblib
- **Data Format**: CSV
- **Language**: Python 3.13
- **Version Control**: Git + GitHub

---

## 📦 Folder Structure

vehicle-price-prediction/
│
├── app.py # Streamlit app
├── models/ # Trained model (joblib file)
│ └── latest_model.joblib
├── requirements.txt # Python dependencies
├── README.md
├── src/
│ ├── config/
│ │ └── config.py # YAML config loader
│ │ └── default.yaml # Config for paths/features
│ ├── data/
│ │ └── raw/
│ │ └── dataset.csv # Vehicle data
│ └── vehicle_price/
│   └── init.py
│   └──train.py # Training script
│   └── features.py # Data processing


---

## 🧪 Run Locally

### Prerequisites:
- Python 3.13+
- pip

### Installation:

git clone https://github.com/abhishek-si-ngh/vehicle-price-prediction.git
cd vehicle-price-prediction
python -m venv .venv
.venv\Scripts\activate         # Windows
pip install -r requirements.txt

## Train the model (Optional):

set PYTHONPATH=src
python -m vehicle_price.train

## Run Streamlit app:

streamlit run app.py

## 🌐 Deployed Link:

https://vehicle-price-prediction-6nxr.onrender.com

## 🤝 Contributing
Feel free to fork this repo, raise issues, or submit pull requests!

📄 License
MIT License © Abhishek Singh