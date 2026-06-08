# tests/test_validation.py

import pandas as pd
import pytest

from src.validation.schema_validator import (
    SchemaValidator
)

from src.validation.data_validator import (
    DataValidator
)


def test_schema_validation(
    sample_dataframe
):

    assert (
        SchemaValidator
        .validate_columns(
            sample_dataframe
        )
        is True
    )


def test_empty_dataframe():

    df = pd.DataFrame()

    with pytest.raises(
        Exception
    ):

        DataValidator.validate_empty_dataframe(
            df
        )