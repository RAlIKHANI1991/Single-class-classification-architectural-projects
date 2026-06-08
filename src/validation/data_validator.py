# src/validation/data_validator.py

from src.exceptions.custom_exceptions import DataValidationError


class DataValidator:

    @staticmethod
    def validate_empty_dataframe(df):

        if df.empty:

            raise DataValidationError(
                "DataFrame is empty"
            )

        return True

    @staticmethod
    def validate_duplicates(df):

        duplicates = df.duplicated().sum()

        if duplicates > 0:

            print(
                f"Warning: "
                f"{duplicates} duplicates found"
            )

        return True

    @staticmethod
    def validate_missing_values(
        df,
        threshold=0.8
    ):

        missing_ratio = (
            df.isnull()
            .mean()
        )

        problematic_cols = (
            missing_ratio[
                missing_ratio > threshold
            ]
            .index
            .tolist()
        )

        if problematic_cols:

            raise DataValidationError(

                f"Too many missing values: "
                f"{problematic_cols}"
            )

        return True