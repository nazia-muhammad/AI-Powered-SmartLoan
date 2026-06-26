# AI-Powered SmartLoan — Testing Notes

## Endpoint Tested

POST `/loan/evaluate`

Local test URL:

`http://127.0.0.1:8002/loan/evaluate`

## Testing Tools

• Swagger
• Postman

## Test Summary

The API was tested using Swagger and the saved Postman collection SmartLoan API Tests — Iterations 1–6. The endpoint uses Pydantic to validate applicant data before applying rule-based risk checks and returning a structured JSON response.

## Test Cases Covered

| Test Case                               | Input Change                                 | Expected Result                  |
| --------------------------------------- | -------------------------------------------- | -------------------------------- |
| Good Applicant - Approved               | Normal applicant data                        | Approved, Low risk, risk score 0 |
| Missed Payments - Rejected              | `missed_payments = 1`                        | Rejected, Medium risk            |
| Low Credit Score - Rejected             | `credit_score = 520`                         | Rejected, Medium risk            |
| High Debt - Rejected                    | `existing_monthly_debt_payment = 6000`       | Rejected, Medium risk            |
| High Expenses - Rejected                | `monthly_expenses = 8000`                    | Rejected, Medium risk            |
| Loan Amount Too High - Rejected         | `requested_loan_amount = 50000`              | Rejected, Medium risk            |
| Missing Input - Validation Error        | Removed `bank_balance`                       | Validation error                 |
| Invalid Credit Score - Validation Error | `credit_score = 900`                         | Validation error                 |
| Multiple Risk Factors - High Risk       | Low credit score, missed payments, high debt | Rejected, High risk              |
| Underage Applicant - Validation Error   | `age = 16`                                   | Validation error                 |
| Zero Income - Validation Error          | `monthly_income = 0`                         | Validation error                 |
| Negative Expenses - Validation Error    | `monthly_expenses = -1000`                   | Validation error                 |

## Use Case Mapping

The Postman test cases are mapped to the SmartLoan Version 1.0 use cases as follows:

• UC1 — Good Applicant - Approved
• UC2 — Missed Payments - Rejected
• UC3 — Low Credit Score - Rejected
• UC4 — High Debt - Rejected
• UC5 — High Expenses - Rejected
• UC6 — Loan Amount Too High - Rejected
• UC7 — Multiple Risk Factors - High Risk
• UC8 — Missing or Invalid Application Data

UC8 includes:

• Missing Input - Validation Error
• Invalid Credit Score - Validation Error
• Underage Applicant - Validation Error
• Zero Income - Validation Error
• Negative Expenses - Validation Error

The current tests use customer-provided API/JSON data only. SmartLoan Version 1.0 does not verify external documents or third-party data.

## Result

All 12 planned Postman requests returned the expected status codes and JSON responses.

## Current Status

SmartLoan Version 1.0, developed through Iterations 1–6, is working locally through FastAPI and has been tested using Swagger and Postman.

## API Response Fields

The SmartLoan API now includes two additional fields in every response:

• decision_category - identifies whether the result is an approval, rejection, or validation error.
• input_source - records where the application data comes from.

Current values:

• Approved application → decision_category: approval
• Rejection application → decision_category: rejection
• Invalid application → decision_category: validation_error 
• Current input source → input_source: customer_api_json

These fields improve response clarity and prepare the system for future input sources. 

## Regression Test Results

The SmartLoan API Tests — Iterations 1–6 Postman collection was rerun after adding Pydantic validation, response models, decision_category, and input_source.

All 12 saved requests returned the expected status codes and JSON responses:

• UC1 — Good Applicant Approved
• UC2 — Missed Payments Rejected
• UC3 — Low Credit Score Rejected
• UC4 — High Debt Rejected
• UC5 — High Expenses Rejected
• UC6 — Loan Amount Too High Rejected
• UC7 — Multiple Risk Factors High Risk
• UC8 — Missing Input
• UC8 — Invalid Credit Score
• UC8 — Underage Applicant
• UC8 — Zero Income
• UC8 — Negative Expenses

Valid applications returned the expected approval or rejection decision. Invalid applications returned validation errors without producing a loan decision.

The Postman Collection Runner completed with no request errors. The collection currently contains no automated Postman test scripts. Automated Python tests will be added using Pytest in Iteration 7.
