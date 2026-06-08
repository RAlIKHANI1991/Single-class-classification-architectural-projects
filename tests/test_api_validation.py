# tests/test_api_validation.py

from fastapi.testclient import TestClient
from api.app import app

client = TestClient(app)

# test 1 نبودن Name
def test_missing_name():

    payload = {
        "Pclass": 3,
        "Sex": "male",
        "Age": 22,
        "SibSp": 1,
        "Parch": 0,
        "Fare": 7.25,
        "Embarked": "S"
    }

    response = client.post(
        "/predict",
        json=payload
    )

    assert response.status_code == 422

# test 2  نوع داده اشتباه
def test_invalid_age_type():

    payload = {
        "Pclass": 3,
        "Name": "Braund, Mr. Owen Harris",
        "Sex": "male",
        "Age": "twenty two",
        "SibSp": 1,
        "Parch": 0,
        "Fare": 7.25,
        "Embarked": "S"
    }

    response = client.post(
        "/predict",
        json=payload
    )

    assert response.status_code == 422
   

# test3 نبودن کل Payload
def test_empty_payload():

    response = client.post(
        "/predict",
        json={}
    )

    assert response.status_code == 422


# test 4 فیلد اضافی
def test_extra_field():

    payload = {
        "Pclass": 3,
        "Name": "Braund, Mr. Owen Harris",
        "Sex": "male",
        "Age": 22,
        "SibSp": 1,
        "Parch": 0,
        "Fare": 7.25,
        "Embarked": "S",
        "UnknownField": 123
    }

    response = client.post(
        "/predict",
        json=payload
    )

    assert response.status_code == 200
