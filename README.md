# AI-Powered SmartLoan

## Project Overview

AI-Powered SmartLoan is a Stage 1 backend prototype for evaluating basic loan eligibility and risk.

The prototype accepts customer loan application data, validates the input, applies simple rule-based risk checks and returns a structured JSON response with:

• Decision: Approved or Rejected
• Risk level: Low, Medium or High
• Risk score
• Reasons for the decision
• Validation errors when input is missing or invalid

This version is focused on backend logic and API testing only.

## Current Scope

This prototype includes:

• Python loan evaluation logic
• Input validation
• Rule-based risk scoring
• FastAPI backend
• POST API endpoint for loan evaluation
• Swagger testing
• Postman test collection
• Testing notes

## Automated Decision Policy

SmartLoan Stage 1 makes loan decisions automatically without a human loan officer or manual review.

The current decision policy is:

• Approved: The application is valid and no risk factors are identified.
• Rejected: The application is valid but one or more risk factors are identified.
• Validation Error: Required data is missing or invalid, so the system does not make an approval or rejection decision.

The current system does not use:

• Manual review
•  Loan officer approval
•  Review Required
• More Information Required

All current decisions are made automatically using validation rules and rule-based risk checks.

## Current Limitations

The current Stage 1 prototype does not include:

Database storage
Frontend user interface
Real bank integrations
Real credit bureau checks
Employer or KYC verification
PDF, image, or CSV/Excel processing
Manual review workflow
Full AI/ML model
Production-level authentication and security

## Use Cases

The current Postman tests are mapped to these Stage 1 use cases:

UC1 — Good Applicant - Approved
UC2 — Missed Payments - Rejected
UC3 — Low Credit Score - Rejected
UC4 — High Debt - Rejected
UC5 — High Expenses - Rejected
UC6 — Loan Amount Too High - Rejected
UC7 — Multiple Risk Factors - High Risk
UC8 — Missing or Invalid Application Data

## Current Input Source

The current Stage 1 prototype uses customer-provided API/JSON data only.

The system validates the submitted values and applies rule-based eligibility and risk checks. It does not currently verify information through external documents or third-party systems.

## Future Input Sources

Future stages may explore:

Synthetic or sandbox bank transaction data
Mock credit bureau data
Mock employer and KYC verification data
PDF documents such as bank statements and payslips
Images such as ID cards and document screenshots
CSV/Excel applicant and financial records

These sources are future scope and are not processed by the current Stage 1 prototype.

## Project Files

| File               | Purpose                                               |
| ------------------ | ----------------------------------------------------- |
| `loan_logic.py`    | Contains validation, risk scoring, and decision logic |
| `main.py`          | Contains the FastAPI app and API routes               |
| `TESTING_NOTES.md` | Contains the Postman testing summary and test cases   |

## API Endpoint

### Health Check

GET `/`

Returns a basic message confirming that the API is running.

### Loan Evaluation

POST `/loan/evaluate`

Local URL:

`http://127.0.0.1:8002/loan/evaluate`

The endpoint accepts applicant data as JSON and returns the loan evaluation result.

## Sample Request

```json
{
  "age": 28,
  "monthly_income": 12000,
  "monthly_expenses": 4000,
  "existing_loan_amount": 5000,
  "existing_monthly_debt_payment": 1000,
  "employment_status": "employed",
  "employment_duration": 24,
  "credit_score": 720,
  "bank_balance": 8000,
  "missed_payments": 0,
  "requested_loan_amount": 20000,
  "requested_loan_duration": 12
}
```

## Sample Response

```json
{
  "decision": "Approved",
  "risk_level": "Low",
  "risk_score": 0,
  "reasons": [
    "Existing debt level is acceptable.",
    "Monthly expenses are acceptable.",
    "Credit score is acceptable.",
    "No missed payments found.",
    "Requested loan amount is acceptable."
  ]
}
```

## How to Run the Project

From the project folder, run:

```bash
uvicorn main:app --reload --port 8002
```

Then open:

`http://127.0.0.1:8002/docs`

or test the API in Postman using:

`POST http://127.0.0.1:8002/loan/evaluate`

## Testing Summary

The API was tested using Swagger and Postman.

Postman test cases include:

• Good applicant → Approved
• Missed payments → Rejected
• Low credit score → Rejected
• High debt → Rejected
• High expenses → Rejected
• Requested loan amount too high → Rejected
• Missing input → Validation error
• Invalid credit score → Validation error 
• Multiple risk factors → High risk
• Underage applicant → Validation error
• Zero income → Validation error
• Negative expenses → Validation error

All planned Postman test cases returned the expected JSON responses.

## Current Status

The Stage 1 backend prototype is working locally through FastAPI and has been tested using Postman.

## Next Possible Improvements

• Add more detailed repayment ability logic
• Add structured request/response models using Pydantic
• Add automated Python test cases
• Add database storage later if required
• Add future evidence verification logic in a later stage
