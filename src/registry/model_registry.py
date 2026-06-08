# src/registry/model_registry.py

from pathlib import Path
from src.utils.io import  save_json
from src.registry.version_manager import VersionManager
from src.registry.artifact_manager import ArtifactManager
from config.paths import ARTIFACTS_DIR


class ModelRegistry:

    def __init__(self,registry_path):
        self.registry_path = (Path(registry_path))
        self.artifact_manager = (ArtifactManager(ARTIFACTS_DIR))

    def register_model(self,model,metric_name,metric_value):
        version = (VersionManager.generate_version())
        metadata = {
            "version": version,
            "metric": metric_name,
            "score": float(metric_value),
            "stage": "champion"
        }

        self.artifact_manager.save_pipeline(
            pipeline=model,
            metadata=metadata,
            stage="champion"
        )

        save_json(metadata,self.registry_path)

        return metadata


'''
from pathlib import Path

from src.utils.io import (
    save_json,
    load_json
)

from src.registry.version_manager import (
    VersionManager
)

from src.registry.artifact_manager import (
    ArtifactManager
)

from config.paths import (
    ARTIFACTS_DIR
)


class ModelRegistry:

    def __init__(self, registry_path):

        self.registry_path = Path(
            registry_path
        )

        self.artifact_manager = (
            ArtifactManager(
                ARTIFACTS_DIR
            )
        )

    def register_model(
        self,
        model,
        metric_name,
        metric_value
    ):

        version = (
            VersionManager.generate_version()
        )

        metadata = {
            "version": version,
            "metric": metric_name,
            "score": float(metric_value),
            "stage": "champion"
        }

        self.artifact_manager.save_pipeline(
            pipeline=model,
            metadata=metadata,
            stage="champion"
        )

        save_json(
            metadata,
            self.registry_path
        )

        return metadata
'''
'''from pathlib import Path

from src.utils.io import save_json,save_model
from src.registry.version_manager import VersionManager

class ModelRegistry:

    def __init__(self, registry_path):
        self.registry_path = Path(registry_path)

    def register_model(self,model,metric_name,metric_value):
        
        version = VersionManager.generate_version()
        model_dir = (Path("artifacts")/ "model"/ "champion")
        model_dir.mkdir(parents=True,exist_ok=True)
        model_path = (model_dir/ "pipeline.pkl")

        save_model(model,model_path)

        metadata = {
            "version": version,
            "metric": metric_name,
            "score": float(metric_value),
            "stage": "Production",
            "model_path": str(model_path)
        }

        save_json(metadata,self.registry_path)

        return metadata
'''
