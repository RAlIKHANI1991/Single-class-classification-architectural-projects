# tests/test_api.py

from fastapi.testclient import TestClient
from api.app import app

client = TestClient(app)

def test_prediction_endpoint():

    payload = {
        "Pclass": 3,
        "Name": "Braund, Mr. Owen Harris",
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

    assert response.status_code == 200

    result = response.json()

    assert "prediction" in result
    assert "probability" in result

    assert isinstance(
        result["prediction"],
        int
    )

    assert isinstance(
        result["probability"],
        float
    )



# tests/test_api.py

def test_prediction_invalid_payload():

    payload = {
        "Pclass": "wrong_type"
    }

    response = client.post(
        "/predict",
        json=payload
    )

    assert response.status_code == 422