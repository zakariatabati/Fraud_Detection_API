from fastapi import FastAPI
from app.schemas import Transaction,Fraud_detection_predict
import app.model as model
import numpy as np
import pandas as pd

app = FastAPI()

@app.post("/predict",response_model=Fraud_detection_predict)
def predict(transaction:Transaction):
    #transaction_values = np.array(list(transaction.dict().values())).reshape(1, -1)
    transaction_df = pd.DataFrame([transaction.model_dump()])
    is_fraud,is_fraud_proba = model.predict(transaction_df)
    return Fraud_detection_predict(is_Fraud=bool(is_fraud),is_Fraud_Probability=float(is_fraud_proba.ravel()[0]) )
