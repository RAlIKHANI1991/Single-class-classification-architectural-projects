# src/models/trainer.py

from sklearn.model_selection import GridSearchCV
from src.pipelines.model_pipeline import get_model,build_model_pipeline
from config.params import MODEL_CONFIGS,CV,SCORING

# این فایل قلب پروژه است.

class ModelTrainer:

    def __init__(self,feature_pipeline,preprocessor):
        self.feature_pipeline = (feature_pipeline)
        self.preprocessor = (preprocessor)

    def train_model(self,model_key,X_train,y_train):

        config = MODEL_CONFIGS[model_key]
        model = get_model(model_key)
        pipeline = (build_model_pipeline(self.feature_pipeline, self.preprocessor, model))
        
        grid_search = GridSearchCV(estimator=pipeline, param_grid=config["params"],
                                   cv=CV, scoring=SCORING, n_jobs=-1, verbose=1)
        grid_search.fit(X_train,y_train)

        return grid_search

    def train_all_models(self,X_train,y_train):

        results = {}
        for model_key in MODEL_CONFIGS:
            print(f"\nTraining {model_key}")
            search = self.train_model(model_key,X_train,y_train)

            results[model_key] = search

        return results


