# src/pipelines/feature_pipeline.py

from sklearn.pipeline import Pipeline

from src.features.family_size import FamilySizeTransformer
from src.features.title_extractor import TitleExtractorTransformer


def build_feature_pipeline():

    return Pipeline(
        steps=[
            ("family_size",FamilySizeTransformer()),
            ("title_extractor",TitleExtractorTransformer())
        ]
    )


#Feature Layer را به Pipeline متصل می‌کند.