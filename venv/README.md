# Risk Score Calculator API

## Objective
This API calculates a risk score based on violations during an interview.

## Tech Used
- Python
- FastAPI

## Endpoint
POST /calculate-risk

## Input Example
{
  "violations": [
    {"type": "phone", "severity": 0.8},
    {"type": "tab_switch", "severity": 0.5}
  ]
}

## Output Example
{
  "risk_score": 0.9,
  "status": "flagged"
}

## How to Run
1. Activate venv:
   venv\Scripts\activate

2. Install dependencies:
   pip install -r requirements.txt

3. Run server:
   python -m uvicorn main:app --reload

4. Open browser:
   http://127.0.0.1:8000/docs