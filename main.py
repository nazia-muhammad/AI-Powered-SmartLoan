from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from loan_logic import evaluate_loan_application
from models import (
    LoanApplicationRequest,
    LoanDecisionResponse,
    LoanValidationErrorResponse
)
app = FastAPI()

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError
):
    errors = []

    for error in exc.errors():
        field_name = error["loc"][-1]
        message = error["msg"]
        errors.append(f"{field_name}: {message}")

    response = LoanValidationErrorResponse(
        is_valid=False,
        errors=errors,
        decision_category="validation_error",
        input_source="customer_api_json"
    )

    return JSONResponse(
        status_code=422,
        content=response.model_dump()
    )
@app.get("/")
def home():
    return {"message": "SmartLoan API is running"}

@app.post("/loan/evaluate", response_model=LoanDecisionResponse)
def evaluate_loan(applicant: LoanApplicationRequest):
    applicant_data = applicant.model_dump()
    result = evaluate_loan_application(applicant_data)
    return result

