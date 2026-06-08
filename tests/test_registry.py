# tests/test_registry.py

from src.registry.artifact_manager import ArtifactManager
from config.paths import ARTIFACTS_DIR


def test_pipeline_exists():
    manager = ArtifactManager(ARTIFACTS_DIR)

    assert manager.pipeline_exists(stage="champion")