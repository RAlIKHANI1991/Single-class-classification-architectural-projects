import mlflow

mlflow.set_tracking_uri("http://localhost:5000")

mlflow.set_experiment("Titanic_Test")

with mlflow.start_run():

    mlflow.log_param("model", "RandomForest")

    mlflow.log_param("depth", 10)

    mlflow.log_metric("accuracy", 0.85)

print("Done")