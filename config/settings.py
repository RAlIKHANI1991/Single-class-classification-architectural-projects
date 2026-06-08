# config/settings.py

from dataclasses import dataclass

@dataclass
class Settings:

    APP_NAME: str = "Titanic Prediction API"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = False
    LOG_LEVEL: str = "INFO"

settings = Settings()