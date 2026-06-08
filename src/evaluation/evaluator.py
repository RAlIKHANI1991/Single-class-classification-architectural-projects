# src/evaluation/evaluator.py

from src.evaluation.metrics import MetricsCalculator


class ModelEvaluator:

    @staticmethod
    def evaluate_model(model, X_test, y_test):

        predictions = (model.predict(X_test))
        probabilities = (model.predict_proba(X_test)[:, 1])

        metrics = (MetricsCalculator.calculate_metrics(y_test,predictions,probabilities))

        return metrics
    
'''
این فایل مهم‌ترین فایل Evaluation Layer است.



'''