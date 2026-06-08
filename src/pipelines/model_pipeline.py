# src/pipelines/model_pipeline.py

from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier


def get_model(model_name):
    models = {
        "lr":LogisticRegression(),
        "rf":RandomForestClassifier(),
        "xgb":XGBClassifier()
    }

    return models[model_name]


def build_model_pipeline(feature_pipeline,preprocessor,model):

    pipeline = Pipeline(steps=[ ("feature_engineering",feature_pipeline),
                                ("preprocessing",preprocessor),
                                ("model",model)
        ])

    return pipeline



# این مهم‌ترین فایل کل پروژه است.