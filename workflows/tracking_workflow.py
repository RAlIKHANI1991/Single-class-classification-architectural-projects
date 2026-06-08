# workflows/tracking_workflow.py

from src.experiments.run_manager import experiment_run

class TrackingWorkflow:
    """
    ثبت اطلاعات در MLflow
    """

    @staticmethod
    def run(model_name,search,metrics):

        with experiment_run(model_name) as tracker:

            tracker.log_params(search.best_params_)
            tracker.log_metrics(metrics)
            tracker.log_model(search.best_estimator_)