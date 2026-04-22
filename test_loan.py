import pytest

from loan import app

@pytest.fixture
def client():
    return app.test_client()

def test_home(client):
    resp = client.get('/')
    assert resp.status_code == 200
    assert resp.text == "<h1>Welcome to Loan API</h1>"

def test_predict_million(client):
    data = {
    "Gender": "Male",
    "Married": "Unmarried",
    "ApplicantIncome": 500,
    "LoanAmount": 100000,
    "Credit_History": 1
   }

    resp = client.post('/predict', json=data)
    assert resp.status_code == 200
    assert resp.json['loan_approval_status'] == "Loan is Rejected"