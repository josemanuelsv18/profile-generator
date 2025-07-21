from abc import ABC, abstractmethod
import json

class Generator(ABC):
    def __init__(self):
        pass
    def read_json(self, route):
        with open(route, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    
    @abstractmethod
    def generate(self):
        pass