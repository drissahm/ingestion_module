from sources.gcs_source import GCSSource
from sources.google_drive_source import GoogleDriveSource
from helpers.pandas_utils import generate_pandas_schema

def build_source(source_cfg: dict, table_cfg: dict):
    stype = source_cfg["type"]
    table_schema = generate_pandas_schema(table_cfg["schema"])
    table_sep  = table_cfg["sep"]
    
    if stype == "gcs":
        return GCSSource(
            bucket_name=source_cfg["bucket_name"],
            object_name=table_cfg["object_name"],
            schema = table_schema,
            sep = table_sep
        )

    if stype == "google_drive":
        sep = table_cfg["sep"]
        return GoogleDriveSource(
            file_id=table_cfg["file_id"],
            schema = table_schema,
            sep= table_sep
        )

    raise ValueError(f"Unsupported source type: {stype}")