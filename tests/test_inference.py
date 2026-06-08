# tests/test_inference.py

from inference.model_loader import ModelLoader


def test_load_champion():
    
    loader = ModelLoader()
    pipeline = loader.load_champion()
    assert pipeline is not None