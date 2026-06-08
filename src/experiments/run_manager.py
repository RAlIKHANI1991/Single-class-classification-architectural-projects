# src/experiments/run_manager.py

from contextlib import contextmanager
from src.experiments.tracking import ExperimentTracker


@contextmanager
def experiment_run(run_name):

    tracker = ( ExperimentTracker())

    with tracker.start_run(run_name):
        yield tracker



'''
حالا هر Workflow می‌تواند بنویسد:

with experiment_run("rf_run") as tracker:
    tracker.log_params(...)
    tracker.log_metrics(...)
    tracker.log_model(...)
    
'''