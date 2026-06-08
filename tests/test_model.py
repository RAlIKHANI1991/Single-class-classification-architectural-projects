# tests/test_model.py

import pandas as pd

from sklearn.model_selection import (
    train_test_split
)

from src.models.trainer import (
    ModelTrainer
)

from src.pipelines.feature_pipeline import (
    build_feature_pipeline
)

from src.pipelines.preprocessing import (
    build_preprocessor
)


def test_training_runs(
    sample_dataframe
):

    X = sample_dataframe.drop(
        columns=["Survived"]
    )

    y = sample_dataframe[
        "Survived"
    ]

    numeric_features = [
        "Age",
        "Fare",
        "SibSp",
        "Parch"
    ]

    categorical_features = [
        "Sex",
        "Embarked"
    ]

    trainer = ModelTrainer(

        build_feature_pipeline(),

        build_preprocessor(
            numeric_features,
            categorical_features
        )
    )

    results = (
        trainer.train_all_models(
            X,
            y
        )
    )

    assert len(results) > 0