# src/validation/feature_validator.py

from src.exceptions.custom_exceptions import DataValidationError

class FeatureValidator:

    @staticmethod
    def validate_feature_schema(df,schema):

        expected = set()
        expected.update(schema["numeric_features"])
        expected.update(schema["categorical_features"])
        expected.update(schema["id_columns"])
        expected.add(schema["target"])
        actual = set(df.columns)
        missing = expected - actual

        if missing:
            raise DataValidationError(f"Missing Features: "f"{missing}")

        return True