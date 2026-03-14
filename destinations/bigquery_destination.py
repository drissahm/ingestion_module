from google.cloud import bigquery
from  destinations.abstract_destination import AbstractDestination
import pandas as pd

class BigQueryDestination(AbstractDestination):
    def __init__(self, project_id: str, dataset_id: str, table_id: str, location: str = "EU", mode: str = "append"):
        self.project_id = project_id
        self.dataset_id = dataset_id
        self.table_id = table_id
        self.location = location
        self.mode = mode

    def write(self, df: pd.DataFrame):
        client = bigquery.Client(project=self.project_id)

        disposition_map = {
            "append": bigquery.WriteDisposition.WRITE_APPEND,
            "replace": bigquery.WriteDisposition.WRITE_TRUNCATE,
            "fail": bigquery.WriteDisposition.WRITE_EMPTY,
        }

        job_config = bigquery.LoadJobConfig(
            write_disposition=disposition_map[self.mode],
            autodetect=True,
        )

        table_ref = f"{self.project_id}.{self.dataset_id}.{self.table_id}"

        job = client.load_table_from_dataframe(df, table_ref, job_config=job_config, location=self.location)
        job.result()