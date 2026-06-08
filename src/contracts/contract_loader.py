# src/contracts/contract_loader.py

from src.utils.io import load_json


class ContractLoader:

    @staticmethod
    def load(path):

        return load_json(path)
    
'''
وظیفه

بارگذاری تمام قراردادها
'''