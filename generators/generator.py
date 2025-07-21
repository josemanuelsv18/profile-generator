from abc import ABC, abstractmethod
import json
import os

class Generator(ABC):
    def __init__(self):
        pass
    def read_json(self, route):
        # Build absolute path based on current file location
        base_dir = os.path.dirname(os.path.abspath(__file__))
        abs_path = os.path.join(base_dir, route)
        with open(abs_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    
    @abstractmethod
    def generate(self):
        pass