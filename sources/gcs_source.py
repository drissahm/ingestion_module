from sources.abstract_source import AbstractSource
import pandas as pd


class GCSSource(AbstractSource):
    def __init__(self, bucket_name: str, object_name: str, sep: str = ","):
        self.bucket_name = bucket_name
        self.object_name = object_name
        self.sep = sep
    
    def read(self):
        gcs_uri = f"gs://{self.bucket_name}/{self.object_name}"
        return pd.read_csv(gcs_uri, sep=self.sep)