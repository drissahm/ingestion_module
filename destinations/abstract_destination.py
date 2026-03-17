from abc import ABC, abstractmethod
import pandas as pd

class AbstractDestination(ABC):
    @abstractmethod
    def write(self, df: pd.DataFrame) -> None:
        """Consume records"""
        pass

