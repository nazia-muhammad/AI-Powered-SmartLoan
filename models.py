from pydantic import BaseModel, Field


class LoanApplicationRequest(BaseModel):
    age: int = Field(..., ge=18)
    monthly_income: float = Field(..., gt=0)
    monthly_expenses: float = Field(..., ge=0)
    existing_loan_amount: float = Field(..., ge=0)
    existing_monthly_debt_payment: float = Field(..., ge=0)
    employment_status: str
    employment_duration: int
    credit_score: int = Field(..., ge=300, le=850)
    bank_balance: float
    missed_payments: int = Field(..., ge=0)
    requested_loan_amount: float = Field(..., gt=0)
    requested_loan_duration: int = Field(..., gt=0)


class LoanDecisionResponse(BaseModel):
    decision: str
    decision_category: str
    risk_level: str
    risk_score: int
    reasons: list[str]
    input_source: str
    
class LoanValidationErrorResponse(BaseModel):
    is_valid: bool
    errors: list[str]
    decision_category: str
    input_source: str