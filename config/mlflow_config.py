# config/mlflow_config.py

import os

MLFLOW_TRACKING_URI = os.getenv("MLFLOW_TRACKING_URI","sqlite:///mlflow.db")

EXPERIMENT_NAME        = "Titanic_Experiment"
REGISTERED_MODEL_NAME  = "Titanic_Best_Model"