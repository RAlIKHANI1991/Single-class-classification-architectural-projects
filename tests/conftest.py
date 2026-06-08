# tests/conftest.py

import pytest
import pandas as pd


@pytest.fixture
def sample_dataframe():

    return pd.DataFrame({

        "PassengerId": [1, 2, 3],

        "Pclass": [1, 2, 3],

        "Name": [
            "Smith, Mr. John",
            "Jane, Mrs. Alice",
            "Tom, Master. Bob"
        ],

        "Sex": [
            "male",
            "female",
            "male"
        ],

        "Age": [
            25,
            30,
            12
        ],

        "SibSp": [
            1,
            0,
            2
        ],

        "Parch": [
            0,
            1,
            1
        ],

        "Fare": [
            50,
            80,
            30
        ],

        "Embarked": [
            "S",
            "C",
            "Q"
        ],

        "Survived": [
            1,
            0,
            1
        ]
    })