# src/contracts/schema_registry.py

from config.paths import FEATURE_SCHEMA_FILE
from src.contracts.contract_loader import ContractLoader


class SchemaRegistry:

    @staticmethod
    def get_feature_schema():

        return ContractLoader.load(FEATURE_SCHEMA_FILE)
    
'''
وظیفه

مرکز دسترسی به تمام قراردادها
'''