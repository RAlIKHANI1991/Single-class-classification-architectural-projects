# src/models/predictor.py

class Predictor:
    @staticmethod
    def predict(model,X):

        return model.predict(X)

    @staticmethod
    def predict_proba(model,X):

        return model.predict_proba(X)