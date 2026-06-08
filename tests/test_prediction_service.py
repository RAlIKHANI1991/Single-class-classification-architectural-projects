# tests/test_prediction_service.py

from services.prediction_service import PredictionService

def test_prediction_service_creation():
    service = (PredictionService())

    assert service is not None