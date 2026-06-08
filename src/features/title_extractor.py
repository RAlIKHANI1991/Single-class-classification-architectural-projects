# src/features/title_extractor.py

import re
from src.features.base_transformer import BaseFeatureTransformer


class TitleExtractorTransformer(BaseFeatureTransformer):

    @staticmethod
    def extract_title(name):
        title_search = re.search(r" ([A-Za-z]+)\.", name)

        if title_search:
            return title_search.group(1)

        return "Unknown"


    def transform(self, X):

        X = X.copy()
        X["Title"] = (X["Name"].apply(self.extract_title))

        return X