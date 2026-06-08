# src/utils/helpers.py

import pandas as pd


def get_missing_report(df):
    return (df.isnull().sum().sort_values(ascending=False))


def get_shape(df):
    return df.shape


def get_columns(df):
    return df.columns.tolist()