# src/utils/schema_loader.py

from src.utils.io import load_json


class SchemaLoader:

    @staticmethod
    def load_feature_schema(path):

        return load_json(path)