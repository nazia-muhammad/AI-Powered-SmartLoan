# AI-Powered SmartLoan — Testing Notes

## Endpoint Tested

POST `/loan/evaluate`

Local test URL:

`http://127.0.0.1:8002/loan/evaluate`

## Testing Tool

Postman

## Test Summary

The API was tested using a saved Postman collection. The endpoint accepts applicant data as JSON, validates the input, applies rule-based risk checks, and returns a JSON response with decision, risk level, risk score, reasons, or validation errors.

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

## Result

All planned Postman test cases returned the expected JSON responses.

## Current Status

The Stage 1 backend prototype is working locally through FastAPI and has been tested using Postman.
