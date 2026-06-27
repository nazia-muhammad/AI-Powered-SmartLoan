# Import BaseModel to create structured data models
# Import Field to add validation rules to model fields
from pydantic import BaseModel, Field

# This model defines the customer loan application request
# It controls what input data the API accepts
class LoanApplicationRequest(BaseModel):
    # Applicant must be at least 18 years old
    age: int = Field(..., ge=18)

    # Monthly income must be greater than 0
    monthly_income: float = Field(..., gt=0)

    # Monthly expenses can be 0 or more, but cannot be negative
    monthly_expenses: float = Field(..., ge=0)

     # Existing loan amount can be 0 or more
    existing_loan_amount: float = Field(..., ge=0)

    # Existing monthly debt payment can be 0 or more
    existing_monthly_debt_payment: float = Field(..., ge=0)

    # Employment status is provided as text, for example "employed"
    employment_status: str

    # Employment duration is provided as a number
    employment_duration: int

    # Credit score must be between 300 and 850
    credit_score: int = Field(..., ge=300, le=850)

    # Current bank balance is provided as a number
    bank_balance: float

    # Missed payments can be 0 or more
    missed_payments: int = Field(..., ge=0)

    # Requested loan amount must be greater than 0
    requested_loan_amount: float = Field(..., gt=0)

    # Requested loan duration must be greater than 0
    requested_loan_duration: int = Field(..., gt=0)

# This model defines the normal API response
# It is used when the loan application is successfully evaluated
class LoanDecisionResponse(BaseModel):
    # Final loan decision: Approved or Rejected
    decision: str

    # Decision type: approval or rejection
    decision_category: str

    # Risk level: Low, Medium, or High
    risk_level: str

    # Numeric risk score calculated by the loan logic
    risk_score: int

    # List of reasons explaining the decision
    reasons: list[str]

     # Shows where the input data came from
    input_source: str
    
# This model defines the validation error response
# It is used when the customer sends missing or invalid input
class LoanValidationErrorResponse(BaseModel):
    # Shows that the submitted input is not valid
    is_valid: bool

     # List of validation error messages
    errors: list[str]

    # Decision category for validation failures
    decision_category: str

    # Shows where the input data came from
    input_source: str