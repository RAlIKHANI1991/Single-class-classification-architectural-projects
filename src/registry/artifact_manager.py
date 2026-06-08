# src/registry/artifact_manager.py

from pathlib import Path
from src.utils.io import (
    save_model,
    load_model,
    save_json,
    load_json
)


class ArtifactManager:
    """
    مدیریت ذخیره و بارگذاری Artifacts
    """

    def __init__(self, artifacts_root):

        self.artifacts_root = Path(artifacts_root)

    def _get_stage_dir(self, stage):

        return (
            self.artifacts_root
            / "model"
            / stage
        )

    def save_pipeline(
        self,
        pipeline,
        metadata,
        stage="champion"
    ):

        model_dir = self._get_stage_dir(stage)

        model_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        pipeline_path = (
            model_dir
            / "pipeline.pkl"
        )

        metadata_path = (
            model_dir
            / "metadata.json"
        )

        save_model(
            pipeline,
            pipeline_path
        )

        save_json(
            metadata,
            metadata_path
        )

        return pipeline_path

    def load_pipeline(
        self,
        stage="champion"
    ):

        pipeline_path = (
            self._get_stage_dir(stage)
            / "pipeline.pkl"
        )

        return load_model(
            pipeline_path
        )

    def load_metadata(
        self,
        stage="champion"
    ):

        metadata_path = (
            self._get_stage_dir(stage)
            / "metadata.json"
        )

        if not metadata_path.exists():
            return None

        return load_json(
            metadata_path
        )

    def pipeline_exists(
        self,
        stage="champion"
    ):

        pipeline_path = (
            self._get_stage_dir(stage)
            / "pipeline.pkl"
        )

        return pipeline_path.exists()


'''
وظیفه
Save Pipeline
Load Pipeline
Archive Pipeline
Promote Champion


چرا؟
الان Registry نباید بداند Joblib چیست.
Registry فقط باید بداند:
Register Model
و ArtifactManager باید بداند:

Save Model
Load Model

اصل Single Responsibility.
'''