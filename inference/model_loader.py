# inference/model_loader.py

from src.utils.io import load_model,load_json
from config.paths import CHAMPION_PIPELINE_FILE,CHALLENGER_PIPELINE_FILE,CHAMPION_METADATA_FILE

class ModelLoader: 
    @staticmethod
    def load_champion():
        return load_model(CHAMPION_PIPELINE_FILE)

    @staticmethod
    def load_challenger():
        return load_model(CHALLENGER_PIPELINE_FILE)

    @staticmethod
    def load_champion_metadata():
        return load_json(CHAMPION_METADATA_FILE)