# src/features/family_size.py

from src.features.base_transformer import BaseFeatureTransformer


class FamilySizeTransformer(BaseFeatureTransformer):

    def transform(self, X):
        X = X.copy()
        X["FamilySize"] = (X["SibSp"] + X["Parch"] + 1 )

        return X