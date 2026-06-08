# src/utils/io.py

import json
import joblib
import pandas as pd


def load_csv(path):
    return pd.read_csv(path)

def save_csv(df, path):
    df.to_csv(path, index=False)

def save_model(model, path):
    joblib.dump(model, path)

def load_model(path):
    return joblib.load(path)

def save_json(data, path):
    with open(path, "w") as f:
        json.dump(data,f,indent=4)

def load_json(path):
    with open(path, "r") as f:
        return json.load(f)