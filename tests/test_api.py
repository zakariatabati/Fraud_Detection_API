import requests
import pandas as pd

API_URL = "http://127.0.0.1:8000/predict"

def test_fraud_detection():
    df = pd.read_csv("test_data.csv")
    df = df[["amt","gender","category"]]
    for _, row in df.iterrows():
        response = requests.post(API_URL, json=row.to_dict())
        assert response.status_code == 200
        assert "is_Fraud" in response.json()  # Check if 'is_Fraud' key exists
        assert "is_Fraud_Probability" in response.json()
