# services/prediction_service.py

import pandas as pd
from inference.model_loader import ModelLoader
from config.logging_config import setup_logger
from src.exceptions.custom_exceptions import PredictionError,ModelNotLoadedError


logger = setup_logger("prediction_service")

class PredictionService:

    def __init__(self):
        try:
            self.pipeline = (ModelLoader.load_champion())
            logger.info("Champion model loaded")

        except Exception as e:
            logger.exception("Model loading failed")
            raise ModelNotLoadedError(str(e))

    def predict(self, data):
        try:
            logger.info("Prediction request received")

            if isinstance(data, dict):
                data = pd.DataFrame([data])

            prediction = (self.pipeline.predict(data))
            probability = (self.pipeline.predict_proba(data))

            result = {
                "prediction": int(prediction[0]),
                "probability": float(
                    probability[0].max()
                )}

            logger.info(
                f"Prediction={result['prediction']} "
                f"Probability={result['probability']:.4f}"
            )

            return result

        except Exception as e:
            logger.exception("Prediction failed")
            raise PredictionError(str(e))

