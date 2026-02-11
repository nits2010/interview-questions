"""
    A utility class to generate unique ids for surveys, questions and options.
"""
from abc import ABC, abstractmethod
import uuid

class IdGenerator(ABC):
    @abstractmethod
    def generate_id(self) -> str:
        pass
