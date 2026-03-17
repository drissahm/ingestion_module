from abc import ABC, abstractmethod
from typing import Iterable, Any

import pandas as pd

class AbstractSource(ABC):
    @abstractmethod
    def read(self) -> pd.DataFrame:
        """Return an iterable of records"""
        pass