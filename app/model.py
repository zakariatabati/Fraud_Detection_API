import joblib
from app.schemas import Transaction

model  = joblib.load("../models/Fraud_detection_model.pkl")

def predict(transaction):
    return (model.predict(transaction),model.predict_proba(transaction))
