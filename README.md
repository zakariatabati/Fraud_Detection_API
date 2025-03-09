# Fraud Transaction Detection API 🚀

## 📌 Project Overview
This project is a **Fraud Transaction Detection API** built using **FastAPI** and **Machine Learning**. It analyzes financial transactions and predicts whether they are fraudulent based on a trained ML model.

## 📂 Project Structure
```
Fraud_Detection_API/
│── app/
│   ├── __init__.py
│   ├── main.py           # FastAPI app entry point
│   ├── model.py          # Machine learning model handling
│   ├── schemas.py        # Pydantic schemas for request/response
│── data/                 # Folder for storing datasets
│── models/               # Folder for saving trained ML models
│── notebooks/            # Jupyter notebooks for EDA model training
│── tests/                # Unit tests for API
│── requirements.txt      # Dependencies
│── README.md             # Project documentation
```

## 🛠 Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/zakariatabati/fraud-detection-api.git
cd fraud-detection-api
```

### 2️⃣ Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate    # Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the FastAPI Server
```bash
cd app
fastapi dev main.py
```

### 5️⃣ Access API Docs
Once the server is running, open:
- 📌 **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- 📌 **Redoc UI:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## 🚀 API Endpoints
| Method | Endpoint      | Description |
|--------|-------------|-------------|
| `POST` | `/predict`   | Predict if a transaction is fraudulent |

### 🏦 Example `POST /predict` Request
```json
{
  "amt": 250.75,
  "Gender": "M",
  "category": "travel"
}
```

### ✅ Example Response
```json
{
  "is_fraud": true,
  "fraud_probability": 0.87
}
```

## 🧠 Machine Learning Model
- The model is trained using **Random Forest**
- The preprocessing pipeline handles **missing values, scaling, and encoding**
- The trained model is saved inside the `models/` directory for predictions

## 🧪 Running Tests
To run unit tests, use:
```bash
pytest tests/test_api.py
```



## ✨ Contributions
Feel free to fork this repo and submit a pull request! 😊

## 📜 License
This project is licensed under the **MIT License**.

