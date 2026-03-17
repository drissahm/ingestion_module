from sources.abstract_source import AbstractSource
import pandas as pd


class LocalCSVSource(AbstractSource):
    def __init__(self, path: str):
        self.path = path

    def read(self):
        return pd.read_csv(self.path)