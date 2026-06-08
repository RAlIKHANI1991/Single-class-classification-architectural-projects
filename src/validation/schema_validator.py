# src/validation/schema_validator.py

from src.exceptions.custom_exceptions import DataValidationError


class SchemaValidator:

    REQUIRED_COLUMNS = [
        "Pclass",
        "Sex",
        "Age",
        "SibSp",
        "Parch",
        "Fare",
        "Embarked",
        "Survived"
    ]

    @classmethod
    def validate_columns(cls, df):

        missing_columns = [col for col in cls.REQUIRED_COLUMNS if col not in df.columns]

        if missing_columns:
            raise DataValidationError(f"Missing Columns: {missing_columns}")

        return True