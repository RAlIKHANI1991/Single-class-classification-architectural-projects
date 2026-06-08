# config/paths.py
from pathlib import Path

# ROOT==================================================
ROOT_DIR = Path(__file__).resolve().parents[1]

# DATA ==================================================
DATA_DIR              = ROOT_DIR / "data"

RAW_DATA_DIR          = DATA_DIR / "raw"
INTERIM_DATA_DIR      = DATA_DIR / "interim"
PROCESSED_DATA_DIR    = DATA_DIR / "processed"


# ARTIFACTS ==================================================
ARTIFACTS_DIR = ROOT_DIR / "artifacts"

MODEL_DIR          = ARTIFACTS_DIR / "model"
CALIBRATION_DIR    = ARTIFACTS_DIR / "calibration"
THRESHOLD_DIR      = ARTIFACTS_DIR / "threshold"
METRICS_DIR        = ARTIFACTS_DIR / "metrics"
FIGURES_DIR        = ARTIFACTS_DIR / "figures"
PREDICTIONS_DIR    = ARTIFACTS_DIR / "predictions"
CV_RESULTS_DIR     = ARTIFACTS_DIR / "cv_results"
REPORTS_DIR        = ARTIFACTS_DIR / "reports"


# MODEL REGISTRY ==================================================
CHAMPION_MODEL_DIR     = MODEL_DIR / "champion"
CHALLENGER_MODEL_DIR   = MODEL_DIR / "challenger"
ARCHIVE_MODEL_DIR      = MODEL_DIR / "archive"


# MODEL FILES ==================================================
CHAMPION_PIPELINE_FILE    = (CHAMPION_MODEL_DIR / "pipeline.pkl")
CHAMPION_METADATA_FILE    = (CHAMPION_MODEL_DIR / "metadata.json")

CHALLENGER_PIPELINE_FILE  = (CHALLENGER_MODEL_DIR / "pipeline.pkl")
CHALLENGER_METADATA_FILE  = (CHALLENGER_MODEL_DIR / "metadata.json")


# CALIBRATION ==================================================
CALIBRATED_MODEL_FILE = (CALIBRATION_DIR / "calibrator.pkl")


# THRESHOLD ==================================================
THRESHOLD_FILE = (THRESHOLD_DIR / "threshold.json")


# METRICS ==================================================
METRICS_FILE      = (METRICS_DIR / "metrics.json")
LEADERBOARD_FILE  = (METRICS_DIR / "leaderboard.csv")


# CV RESULTS ==================================================
CV_RESULTS_FILE = (CV_RESULTS_DIR / "cv_results.csv")


# CONTRACTS ==================================================
CONTRACTS_DIR           = ROOT_DIR / "contracts"

FEATURE_SCHEMA_FILE     = (CONTRACTS_DIR / "feature_schema.json")
API_INPUT_SCHEMA_FILE   = (CONTRACTS_DIR / "api_input_schema.json")
API_OUTPUT_SCHEMA_FILE  = (CONTRACTS_DIR / "api_output_schema.json")
MODEL_SCHEMA_FILE       = (CONTRACTS_DIR / "model_schema.json")
PREDICTION_SCHEMA_FILE  = (CONTRACTS_DIR / "prediction_schema.json")
MONITORING_SCHEMA_FILE  = (CONTRACTS_DIR / "monitoring_schema.json")


















'''# 01_config/paths.py

from pathlib import Path

# Root Project
ROOT_DIR = Path(__file__).resolve().parents[1]

# -----------------------------
# DATA
# -----------------------------
RAW_DATA_DIR         = ROOT_DIR / "data" / "raw"
INTERIM_DATA_DIR     = ROOT_DIR / "data" / "interim"
PROCESSED_DATA_DIR   = ROOT_DIR / "data" / "processed"

# -----------------------------
# ARTIFACTS
# -----------------------------
MODEL_DIR         = ROOT_DIR / "artifacts" / "model"
CALIBRATION_DIR   = ROOT_DIR / "artifacts" / "calibration"
THRESHOLD_DIR     = ROOT_DIR / "artifacts" / "threshold"
METRICS_DIR       = ROOT_DIR / "artifacts" / "metrics"
FIGURES_DIR       = ROOT_DIR / "artifacts" / "figures"
PREDICTIONS_DIR   = ROOT_DIR / "artifacts" / "predictions"
CV_RESULTS_DIR    = ROOT_DIR / "artifacts" / "cv_results"
REPORTS_DIR       = ROOT_DIR / "artifacts" / "reports"

# -----------------------------
# MODEL FILES
# -----------------------------
MODEL_FILE             = (MODEL_DIR / "model.pkl")
CALIBRATED_MODEL_FILE  = (CALIBRATION_DIR / "calibrated_model.pkl")
THRESHOLD_FILE         = (THRESHOLD_DIR / "threshold.json")
METRICS_FILE           = (METRICS_DIR / "metrics.json")
CV_RESULTS_FILE        = (CV_RESULTS_DIR/ "cv_results.csv")  # این فایل بعداً برای تحلیل GridSearch بسیار ارزشمند می‌شود.
FEATURE_SCHEMA_FILE    = (ROOT_DIR/ "contracts"/ "feature_schema.json")

API_INPUT_SCHEMA_FILE  = (ROOT_DIR/ "contracts"/ "api_input_schema.json")
API_OUTPUT_SCHEMA_FILE = (ROOT_DIR/ "contracts"/ "api_output_schema.json")
MODEL_SCHEMA_FILE      = (ROOT_DIR/ "contracts"/ "model_schema.json")
PREDICTION_SCHEMA_FILE = (ROOT_DIR/ "contracts"/ "prediction_schema.json")
MONITORING_SCHEMA_FILE = (ROOT_DIR/ "contracts"/ "monitoring_schema.json")

# ==================================================
# MODEL REGISTRY
# ==================================================
CHAMPION_MODEL_DIR = (MODEL_DIR / "champion")
CHALLENGER_MODEL_DIR = (MODEL_DIR / "challenger")
ARCHIVE_MODEL_DIR = (MODEL_DIR / "archive")


ARTIFACTS_DIR    = ROOT_DIR / "artifacts"
CHAMPION_DIR     = (ARTIFACTS_DIR/ "model"/ "champion")
CHALLENGER_DIR   = (ARTIFACTS_DIR/ "model"/ "challenger")
ARCHIVE_DIR      = (ARTIFACTS_DIR/ "model"/ "archive")

'''