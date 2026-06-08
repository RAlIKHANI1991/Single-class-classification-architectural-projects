# src/features/feature_builder.py

from sklearn.pipeline import Pipeline
from src.features.family_size import FamilySizeTransformer
from src.features.title_extractor import TitleExtractorTransformer


def build_feature_pipeline():
    pipeline = Pipeline(
        steps=[("family_size", FamilySizeTransformer()),
            ("title", TitleExtractorTransformer())
        ]
    )

    return pipeline

# این فایل مهم‌ترین فایل Feature Layer خواهد شد.