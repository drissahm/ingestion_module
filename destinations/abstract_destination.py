from abc import ABC, abstractmethod
import pandas as pd

class AbstractDestination(ABC):
    @abstractmethod
    def write(self, records) -> None:
        """Consume records"""
        pass

