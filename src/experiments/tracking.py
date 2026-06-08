# src/experiments/tracking.py

import mlflow
import mlflow.sklearn
from config.mlflow_config import MLFLOW_TRACKING_URI,EXPERIMENT_NAME


class ExperimentTracker:

    def __init__(self):
        mlflow.set_tracking_uri( MLFLOW_TRACKING_URI)
        mlflow.set_experiment(EXPERIMENT_NAME)

    def start_run(self,run_name=None):

        return mlflow.start_run(run_name=run_name)

    @staticmethod
    def log_params(params):
        mlflow.log_params(params)

    @staticmethod
    def log_metrics(metrics):
        mlflow.log_metrics(metrics)

    @staticmethod
    def log_tags(tags):

        mlflow.set_tags(tags)

    @staticmethod
    def log_model(model,artifact_path="model"):
        mlflow.sklearn.log_model(sk_model=model,artifact_path=artifact_path)

    @staticmethod
    def log_artifact(path):
        mlflow.log_artifact(path)


'''
این فایل قلب MLOps پروژه خواهد بود.


'''