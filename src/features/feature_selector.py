# src/features/feature_selector.py

class FeatureSelector:

    @staticmethod
    def select_columns(df,columns):

        return df[columns]