# src/features/base_transformer.py

from sklearn.base import BaseEstimator,TransformerMixin


class BaseFeatureTransformer(BaseEstimator,TransformerMixin):

    def fit(self, X, y=None):

        return self

    def transform(self, X):

        return X