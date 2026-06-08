# workflows/pipeline_workflow.py

from config.constants import TARGET
from config.paths import  RAW_DATA_DIR
from src.utils.io import load_csv
from src.utils.feature_detector import FeatureDetector
from src.validation.schema_validator import SchemaValidator
from src.validation.data_validator import DataValidator
from src.pipelines.feature_pipeline import build_feature_pipeline
from src.pipelines.preprocessing import build_preprocessor

from workflows.training_workflow import TrainingWorkflow
from workflows.evaluation_workflow import EvaluationWorkflow
from workflows.tracking_workflow import TrackingWorkflow
from workflows.registry_workflow import RegistryWorkflow
#from workflows.deployment_workflow import DeploymentWorkflow


class PipelineWorkflow:
    """
    اجرای End-To-End پروژه
    """

    def run(self):

        # Load Data--------------------------------
        df = load_csv(RAW_DATA_DIR / "titanic.csv")

        # Validation -------------------------------
        SchemaValidator.validate_columns(df)
        DataValidator.validate_empty_dataframe(df)
        DataValidator.validate_duplicates(df)
        DataValidator.validate_missing_values(df)

        # Split X/y--------------------------------
        X = df.drop(columns=[TARGET])
        y = df[TARGET]

        # Feature Pipeline--------------------------------
        feature_pipeline = (build_feature_pipeline())

        # Dynamic Feature Detection--------------------------------
                #numeric_features = ["Age","Fare","SibSp","Parch","Pclass"]  /////hard ccode/////
                #categorical_features = ["Sex","Embarked"]
        detector = FeatureDetector()
        numeric_features      = (detector.get_numeric_features())
        categorical_features  = (detector.get_categorical_features())
        preprocessor          = (build_preprocessor(numeric_features,categorical_features))

        # Training--------------------------------
        trainer = (TrainingWorkflow(feature_pipeline,preprocessor))
        searches, X_test, y_test = (trainer.run(X,y))

        # Evaluation--------------------------------
        evaluation_results = (EvaluationWorkflow.run(searches,X_test,y_test))

        # Tracking--------------------------------
        for model_name, search in (searches.items()):
            TrackingWorkflow.run(model_name,search,evaluation_results[model_name])

        # Registry--------------------------------
        best_model_name, metadata = (RegistryWorkflow.run(
                                        evaluation_results,searches,"artifacts/model_registry.json"))

        # Deployment--------------------------------
        # حذف  DeploymentWorkflow.run(searches[best_model_name].best_estimator_)

        return {
            "best_model":best_model_name,
            "registry":metadata,
            "metrics":evaluation_results[best_model_name]
        }

