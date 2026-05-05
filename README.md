# Risk Score Prediction API

## 🚀 Overview

This project predicts a risk score using a Machine Learning model and exposes it through a FastAPI REST API.

## 🛠 Tech Stack

* Python
* FastAPI
* scikit-learn

## 📦 Features

* Predict risk score from input data
* REST API built with FastAPI
* Interactive API documentation available

## ▶️ How to Run

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## 🔗 API Documentation

After running the server, open:
http://127.0.0.1:8000/docs

## 📌 Endpoint

POST /predict

## 📥 Example Input

```json
{
  "age": 25,
  "income": 50000
}
```

## 📤 Example Output

```json
{
  "risk_score": 0.78
}
```

## 📈 Future Improvements

* Add frontend interface
* Deploy API online
* Improve model accuracy
