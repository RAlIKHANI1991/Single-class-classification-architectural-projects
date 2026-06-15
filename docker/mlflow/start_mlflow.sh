#!/bin/bash

mlflow server \
--host 0.0.0.0 \
--port 5000 \
--backend-store-uri postgresql://mlflow:mlflow123@postgres:5432/mlflow_db \
--default-artifact-root /mlflow/artifacts