# workflows/registry_workflow.py

from src.registry.model_registry import ModelRegistry
from src.evaluation.model_selector import ModelSelector


class RegistryWorkflow:
    """
    ثبت بهترین مدل
    """

    @staticmethod
    def run(evaluation_results,searches,registry_path):

        best_model_name = (ModelSelector.select_best_model(evaluation_results))
        best_search = (searches[best_model_name])
        registry = ModelRegistry(registry_path)

        metadata = (registry.register_model(
                    model=best_search.best_estimator_, 
                    metric_name="roc_auc",
                    metric_value=evaluation_results[best_model_name]["roc_auc"]
                    ))

        return (best_model_name, metadata) 