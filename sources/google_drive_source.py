from sources.abstract_source import AbstractSource
import pandas as pd


class GoogleDriveSource(AbstractSource):
    def __init__(self, file_id: str, schema: dict, sep: str = ","):
        self.file_id = file_id
        self.schema = schema
        self.sep = sep

    def read(self):
        url = f"https://drive.google.com/uc?export=download&id={self.file_id}"
        return pd.read_csv(url, sep=self.sep, dtype = self.schema)
