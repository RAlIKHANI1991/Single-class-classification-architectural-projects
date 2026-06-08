# inference/predictor.py
# حذف این اسکریپت در آینده به دلیل افزونگی 


import pandas as pd

class Predictor:
    def __init__(self, model):
        self.model = model

    def predict(self, data):
        df = pd.DataFrame([data])
        prediction = (self.model.predict(df))
        probability = (self.model.predict_proba(df))

        return {"prediction": int(prediction[0]),
                "probability": float(probability[0].max())}

