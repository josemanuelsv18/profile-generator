from abc import ABC, abstractmethod

class Insertor(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def insert(self):
        pass