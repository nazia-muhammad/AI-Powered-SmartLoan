# Import FastAPI to create the API application
# Import Request so we can handle validation error requests
from fastapi import FastAPI, Request

# Import FastAPI's validation error class
# This is triggered when the request body does not match the Pydantic model
from fastapi.exceptions import RequestValidationError

# Import JSONResponse so we can return a custom JSON error response
from fastapi.responses import JSONResponse

# Import the main loan evaluation function from loan_logic.py
from loan_logic import evaluate_loan_application

# Import Pydantic models from models.py
# These models define request data, successful response data, and validation error data
from models import (
    LoanApplicationRequest,
    LoanDecisionResponse,
    LoanValidationErrorResponse
)

# Create the FastAPI application
app = FastAPI()

# Custom handler for request validation errors
# This runs when the customer sends missing or invalid input
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError
):
# Create an empty list to store readable validation error messages
    errors = []

# Loop through each validation error returned by FastAPI / Pydantic
    for error in exc.errors():
        # Get the field name that caused the error
        field_name = error["loc"][-1]
        # Get the validation message
        message = error["msg"]
        # Add a readable error message to the errors list
        errors.append(f"{field_name}: {message}")

# Create a structured validation error response using the Pydantic model
    response = LoanValidationErrorResponse(
        is_valid=False,
        errors=errors,
        decision_category="validation_error",
        input_source="customer_api_json"
    )
# Return the validation error response with HTTP status code 422
    return JSONResponse(
        status_code=422,
        content=response.model_dump()
    )

# Basic home route to confirm the API is running
@app.get("/")
def home():
    return {"message": "SmartLoan API is running"}

# Main loan evaluation endpoint
# It accepts customer loan application data and returns a loan decision response
@app.post("/loan/evaluate", response_model=LoanDecisionResponse)
def evaluate_loan(applicant: LoanApplicationRequest):
     # Convert the Pydantic request model into a normal Python dictionary
    applicant_data = applicant.model_dump()

     # Send the applicant data to the loan logic function
    result = evaluate_loan_application(applicant_data)

     # Return the final result to the API user
    return result

