# config/constants.py

"""
ثابت‌های پروژه
مواردی که به ندرت تغییر می‌کنند.
"""

TARGET        = "Survived"
RANDOM_STATE  = 42
PROJECT_NAME  = "Titanic_Project"
MODEL_NAME    = "Titanic_Classifier"
MODEL_VERSION = "1.0.0"


# Models Supported
SUPPORTED_MODELS = {
    "lr":"LogisticRegression",
    "rf":"RandomForest",
    "xgb":"XGBoost"
}