from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Violation(BaseModel):
    type: str
    severity: float

class InputData(BaseModel):
    violations: List[Violation]

def calculate_risk(violations):
    if not violations:
        return 0.0
    
    risk = 1
    for v in violations:
        severity = max(0, min(v.severity, 1))  # keep between 0 and 1
        risk *= (1 - severity)
    
    return round(1 - risk, 2)

def get_status(score):
    if score < 0.3:
        return "safe"
    elif score < 0.7:
        return "warning"
    else:
        return "flagged"

@app.get("/")
def home():
    return {"message": "API is running"}

@app.post("/calculate-risk")
def calculate(input_data: InputData):
    risk_score = calculate_risk(input_data.violations)
    status = get_status(risk_score)
    
    return {
        "risk_score": risk_score,
        "status": status
    }