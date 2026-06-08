# workflows/training_workflow.py

from sklearn.model_selection import train_test_split
from config.params import TEST_SIZE
from src.models.trainer import ModelTrainer


class TrainingWorkflow:
    """
    اجرای کامل فرآیند آموزش مدل‌ها
    """

    def __init__(self,feature_pipeline,preprocessor):
        self.trainer = ModelTrainer(feature_pipeline,preprocessor)

    def run(self,X,y):

        X_train, X_test, y_train, y_test = (train_test_split(X,y,test_size=TEST_SIZE,random_state=42,stratify=y))
        results = (self.trainer.train_all_models(X_train,y_train))

        return (results,X_test,y_test)