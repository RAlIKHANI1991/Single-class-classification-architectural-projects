# src/registry/version_manager.py

from datetime import datetime


class VersionManager:

    @staticmethod
    def generate_version():

        return datetime.now().strftime("%Y.%m.%d.%H%M%S")