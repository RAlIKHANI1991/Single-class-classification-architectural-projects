# config/params.py

TEST_SIZE = 0.2
CV = 5
SCORING = "accuracy"

# ==================================================
# MODELS CONFIG
# ==================================================
MODEL_CONFIGS = {
    "lr": {"model": "LogisticRegression",
        "params": {
            "model__C": [0.01, 0.1, 1, 10],
            "model__solver": ["liblinear","lbfgs"]
        }
    },

    "rf": {
    "model": "RandomForest",
        "params": {
            "model__n_estimators": [100, 200, 300],
            "model__max_depth": [5,10,15],
            "model__min_samples_split": [2,5,10]
        }
    },

    "xgb": {
        "model": "XGBoost",
        "params": {
            "model__n_estimators": [100,200,300],
            "model__max_depth": [3,5,7],
            "model__learning_rate": [0.01,0.05,0.1]
        }
    }
}

# ==================================================
# MODEL SELECTION
# ==================================================
PRIMARY_METRIC = "roc_auc"
OPTIMIZATION_METRIC = "f1"

# ==================================================
# EXPERIMENT
# ==================================================
EXPERIMENT_TAGS = {
    "project"   : "Titanic",
    "owner"     : "Khoda",
    "framework" : "scikit-learn"
}