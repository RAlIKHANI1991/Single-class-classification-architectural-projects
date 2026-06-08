# src/exceptions/custom_exceptions.py

class ModelNotLoadedError(Exception):

    def __init__(self,message="Champion model could not be loaded"):
        self.message = message
        super().__init__(self.message)


class PredictionError(Exception):

    def __init__(self,message="Prediction failed"):
        self.message = message
        super().__init__(self.message)