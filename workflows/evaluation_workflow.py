# workflows/evaluation_workflow.py

from src.evaluation.evaluator import ModelEvaluator


class EvaluationWorkflow:
    """
    ارزیابی تمام مدل‌ها
    """

    @staticmethod
    def run(trained_models,X_test,y_test):

        results = {}
        for name, model in (trained_models.items()):
            metrics = (ModelEvaluator.evaluate_model(model.best_estimator_,X_test,y_test))
            results[name] = metrics

        return results