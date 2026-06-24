# Sample customer loan application data
# This is fake test data for one applicant
sample_applicant = {
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
    "requested_loan_duration": 12,
}

# These are the required fields every applicant must provide 
required_fields = [
    "age",
    "monthly_income",
    "monthly_expenses",
    "existing_loan_amount",
    "existing_monthly_debt_payment",
    "employment_status",
    "employment_duration",
    "credit_score",
    "missed_payments",
    "bank_balance",
    "requested_loan_amount",
    "requested_loan_duration"
]


# This function checks whether the input data is complete and valid
def validate_input(applicant):
    errors = []
    
    # Check if any required field is missing
    for field in required_fields:
        if field not in applicant:
            errors.append(f"{field} is required.")
        
    # Check age rule    
    if "age" in applicant and applicant["age"] < 18:
        errors.append("Age must be at least 18.")
        
    # Check income rule 
    if "monthly_income" in applicant and applicant["monthly_income"] <= 0:
        errors.append("Monthly income must be greater than 0.")
    
    # Check expenses rule
    if "monthly_expenses" in applicant and applicant["monthly_expenses"] < 0:
        errors.append("Monthly expenses cannot be negative.")
        
    # Check existing loan amount rule
    if "existing_loan_amount" in applicant and applicant["existing_loan_amount"] < 0:
        errors.append("Existing loan amount cannot be negative.")
    
    # Check existing monthly debt payment rule
    if "existing_monthly_debt_payment" in applicant and applicant["existing_monthly_debt_payment"] < 0:
        errors.append("Existing monthly debt payment cannot be negative.")  
    
     # Check credit score range
    if "credit_score" in applicant and (applicant["credit_score"] < 300 or applicant["credit_score"] > 850):
        errors.append("Credit score must be between 300 and 850.")
    
   # Check missed payments rule
    if "missed_payments" in applicant and applicant["missed_payments"] < 0:
        errors.append("Missed payments cannot be negative.")
    
    # Check requested loan amount rule
    if "requested_loan_amount" in applicant and applicant["requested_loan_amount"] <= 0:
        errors.append("Requested loan amount must be greater than 0.")
        
    # Check requested loan duration rule
    if "requested_loan_duration" in applicant and applicant["requested_loan_duration"] <= 0:
        errors.append("Requested loan duration must be greater than 0.")
        
    # If errors exist, return invalid result 
    if errors:
        return {
            "is_valid": False,
            "errors": errors
        }
        
    # If no errors, input is valid 
    return {
        "is_valid": True,
        "errors": []
        
    }

# This function calculates applicant risk using simple rules
def calculate_risk(applicant):
    risk_score = 0
    reasons = []
    
    # Get income and existing monthly debt
    monthly_income = applicant["monthly_income"]
    monthly_debt = applicant["existing_monthly_debt_payment"]
    
    # Check debt compared to income 
    debt_ratio = monthly_debt / monthly_income
    
    if debt_ratio > 0.4:
        risk_score += 2
        reasons.append("Existing debt is high compared to income.")
    else:
        reasons.append("Existing debt level is acceptable.")
        
    # Check expenses compared to income 
    expense_ratio = applicant["monthly_expenses"] / monthly_income
    
    if expense_ratio > 0.6:
        risk_score += 2 
        reasons.append("Monthly expenses are high compared to income.")
    else:
        reasons.append("Monthly expenses are acceptable.")
        
    # Check credit score risk 
    if applicant["credit_score"] < 600:
        risk_score += 2
        reasons.append("Credit score is low.")
    else:
        reasons.append("Credit score is acceptable.")
        
    # Check missed payments risk 
    if applicant["missed_payments"] > 0:
        risk_score += 2
        reasons.append("Missed payments are present.")
    else:
        reasons.append("No missed payments found.")
        
    # Check requested loan amount compared to income 
    if applicant["requested_loan_amount"] > applicant["monthly_income"] * 3:
        risk_score += 2
        reasons.append("Requested loan amount is high compared to income.")
    else:
        reasons.append("Requested loan amount is acceptable.")
    
    # Convert risk score into risk level
    if risk_score == 0:
        risk_level = "Low"
    elif risk_score <= 3:
        risk_level = "Medium"
    else:
        risk_level = "High" 
      
    # Return risk result
    return {
        "risk_score": risk_score,
        "risk_level": risk_level,
        "reasons": reasons 
    }
    
# This function makes the final loan decision 
def make_decision(risk_result):
    risk_level = risk_result["risk_level"]
    
    # Version 1 rule:
    # Low risk applicants are approved
    # Medium and High risk applicants are rejected
    if risk_level == "Low":
        decision = "Approved"
        decision_category = "approval"
    else:
        decision = "Rejected"
        decision_category = "rejection"
        
    # Return final decision output 
    return {
        "decision": decision,
        "decision_category": decision_category,
        "risk_level": risk_level,
        "risk_score": risk_result["risk_score"],
        "reasons": risk_result["reasons"]
    }
    
# This function controls the full loan evaluation process
def evaluate_loan_application(applicant):
    
    # Step 1: Validate the input first
    validation_result = validate_input(applicant)
    
    # Step 2: If input is invalid, stop and return validation errors
    if validation_result["is_valid"] == False:
        validation_result["decision_category"] = "validation_error"
        validation_result["input_source"] = "customer_api_json"
        return validation_result
    
    # Step 3: If input is valid, calculate risk 
    risk_result = calculate_risk(applicant)
    
    # Step 4: Make final Approved / Rejected decision
    decision_result = make_decision(risk_result)
    decision_result["input_source"] = "customer_api_json"
    
    # Step 5: Return final decision result
    return decision_result
    
# Run the risk calculation first 
#risk_result = calculate_risk(sample_applicant)

# Then make the final decision 
#print(make_decision(risk_result))

# Run the full loan evaluation process 
#print(evaluate_loan_application(sample_applicant))

