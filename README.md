# 🚗 Vehicle Price Prediction App

This project is a **machine learning web application** that predicts the price of a used vehicle based on inputs like **Make**, **Model**, **Year**, and **Mileage**.

Built with **scikit-learn** for modeling and **Streamlit** for an interactive frontend, it's deployed on **Render** for easy access.

---

## 📌 Features

- ML-based prediction using `RandomForestRegressor`
- Interactive web UI using Streamlit
- Dropdowns for **Make** and **filtered Model**
- Simple input form for:
  - Year
  - Mileage
  - Make
  - Model
- Fast price prediction in ₹

---

## 🧠 Tech Stack

| Layer        | Technology              |
|--------------|--------------------------|
| Frontend     | Streamlit               |
| ML Model     | scikit-learn            |
| Language     | Python 3.13             |
| Deployment   | Render                  |
| Dataset      | CSV (Custom vehicle data) |

---

## 🗂️ Folder Structure

```
vehicle-price-prediction/
│
├── app.py                    # Streamlit app
├── models/                   # Trained model file
│   └── latest_model.joblib
├── requirements.txt
├── README.md
├── src/
│   ├── config/
│   │   ├── config.py
│   │   └── default.yaml
│   ├── data/
│   │   └── raw/
│   │       └── dataset.csv
│   └── vehicle_price/
│       ├── __init__.py
│       ├── train.py
│       └── features.py
```

---

## 🧪 Run Locally

### 📋 Prerequisites

- Python 3.13+
- pip

### 🔧 Installation

```bash
git clone https://github.com/abhishek-si-ngh/vehicle-price-prediction.git
cd vehicle-price-prediction
python -m venv .venv
.venv\Scripts\activate  # For Windows
pip install -r requirements.txt
```

---

### 🏋️‍♂️ (Optional) Train the Model

```bash
set PYTHONPATH=src
python -m vehicle_price.train
```

---

### 🚀 Launch the App

```bash
streamlit run app.py
```

Then go to [http://localhost:8501](http://localhost:8501)

---

## 🌐 Live Demo

🔗 **Deployed on Render**: [https://your-render-app-url.com](https://your-render-app-url.com)

> Replace the above with your actual deployed URL.

---

## 📸 App Preview

> *(Optional)* Add a screenshot here by uploading an image and linking it like this:

```markdown
![App Screenshot](screenshot.png)
```

---

## 🤝 Contributing

Feel free to fork the repo, create a branch, and submit a pull request.

---

## 📄 License

MIT License © [Abhishek Singh](https://github.com/abhishek-si-ngh)
