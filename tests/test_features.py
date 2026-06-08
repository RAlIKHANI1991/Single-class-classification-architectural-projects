# tests/test_features.py

from src.features.family_size import (
    FamilySizeTransformer
)

from src.features.title_extractor import (
    TitleExtractorTransformer
)


def test_family_size_feature(
    sample_dataframe
):

    transformer = (
        FamilySizeTransformer()
    )

    transformed = (
        transformer.transform(
            sample_dataframe
        )
    )

    assert (
        "FamilySize"
        in transformed.columns
    )


def test_title_extraction(
    sample_dataframe
):

    transformer = (
        TitleExtractorTransformer()
    )

    transformed = (
        transformer.transform(
            sample_dataframe
        )
    )

    assert (
        "Title"
        in transformed.columns
    )