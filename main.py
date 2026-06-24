from fastapi import FastAPI 
from loan_logic import evaluate_loan_application

app = FastAPI()

@app.get("/")
def home():
    return {"message": "SmartLoan API is running"}

@app.post("/loan/evaluate")
def evaluate_loan(applicant: dict):
    result = evaluate_loan_application(applicant)
    return result

