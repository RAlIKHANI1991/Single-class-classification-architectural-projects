# tests/test_pipeline.py

from src.pipelines.feature_pipeline import (
    build_feature_pipeline
)


def test_feature_pipeline(
    sample_dataframe
):

    pipeline = (
        build_feature_pipeline()
    )

    transformed = (
        pipeline.transform(
            sample_dataframe
        )
    )

    assert (
        "FamilySize"
        in transformed.columns
    )

    assert (
        "Title"
        in transformed.columns
    )