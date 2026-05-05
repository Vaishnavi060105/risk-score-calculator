# Risk Score Calculator API

## Overview
This API calculates a risk score based on violations during an interview.

## Tech Used
- Python
- FastAPI

## Endpoint
POST /calculate-risk

## Example Input
{
  "violations": [
    {"type": "phone", "severity": 0.8},
    {"type": "tab_switch", "severity": 0.5}
  ]
}

## Example Output
{
  "risk_score": 0.9,
  "status": "flagged"
}

## Run
python -m uvicorn main:app --reload