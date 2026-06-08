# api/routes/prediction.py

from fastapi import APIRouter
from fastapi import Depends
from api.dependencies import get_prediction_service
from api.schemas.request import PassengerRequest
from api.schemas.response import PredictionResponse
from services.prediction_service import PredictionService


router = APIRouter(prefix="/predict",tags=["Prediction"])

@router.post("", response_model = PredictionResponse)
def predict(request: PassengerRequest,
            service: PredictionService = Depends(get_prediction_service)):

    result = service.predict(request.model_dump())

    return PredictionResponse(
        prediction=result["prediction"],
        probability=result["probability"]
    )