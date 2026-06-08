# src/contracts/contract_validator.py

from src.exceptions.custom_exceptions import DataValidationError

class ContractValidator:

    @staticmethod
    def validate_columns(dataframe,schema):

        expected = set()
        expected.update(schema.get("numeric_features",[]))
        expected.update(schema.get("categorical_features",[]))
        actual = set(dataframe.columns)
        missing = expected - actual

        if missing:

            raise DataValidationError(

                f"Missing Columns: "
                f"{missing}"
            )

        return True
    
'''
src/contracts/contract_validator.py

این فایل در آینده برای API و Monitoring بسیار مهم می‌شود.
'''