from pydantic import BaseModel,Field


class Transaction(BaseModel):
    amt : float =Field(...,gt=0,description="Transaction amount must be greater than zero")
    gender:str
    category:str

class Fraud_detection_predict(BaseModel):
    is_Fraud:bool
    is_Fraud_Probability:float

