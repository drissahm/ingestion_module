from destinations.bigquery_destination import BigQueryDestination
from destinations.print_destination import PrintDestination


def build_destination(destination_cfg: dict, table_cfg: dict):
    dtype = destination_cfg["type"]

    if dtype == "bigquery":

        return BigQueryDestination(
            project_id=destination_cfg["project_id"],
            dataset_id=destination_cfg["dataset_id"],
            location=destination_cfg["location"],
            
            table_id=table_cfg["name"],
            mode=table_cfg["mode"]
        )

    if dtype == "print":
        return PrintDestination()

    raise ValueError(f"Unsupported destination type: {dtype}")
