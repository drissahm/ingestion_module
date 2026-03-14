from abc import ABC, abstractmethod
from typing import Iterable, Any

import pandas as pd

class AbstractSource(ABC):
    @abstractmethod
    def read(self):
        """Return an iterable of records"""
        pass


class CSVSource(AbstractSource):
    def __init__(self, path: str):
        self.path = path

    def read(self):
        return pd.read_csv(self.path)