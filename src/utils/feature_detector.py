# src/utils/feature_detector.py

from src.utils.schema_loader import SchemaLoader
from config.paths import FEATURE_SCHEMA_FILE

 
class FeatureDetector:

    def __init__(self):
        self.schema = (SchemaLoader.load_feature_schema(FEATURE_SCHEMA_FILE))

    def get_numeric_features(self):
        return self.schema["numeric_features"]

    def get_categorical_features(self):
        return self.schema["categorical_features"]

    def get_target(self):
        return self.schema["target"]

    def get_id_columns(self):
        return self.schema["id_columns"]