# src/pipelines/inference_pipeline.py

from src.utils.io import load_model
from config.paths import MODEL_FILE


class InferencePipeline:
    def __init__(self):
        self.pipeline = load_model(MODEL_FILE)

    def predict(self, X):
        
        return self.pipeline.predict(X)

    def predict_proba(self, X):

        return self.pipeline.predict_proba(X)