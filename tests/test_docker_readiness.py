# tests\test_docker_readiness.py

from pathlib import Path


def test_champion_model_exists():

    model_path = Path("artifacts/model/champion/pipeline.pkl")

    assert model_path.exists()