from sources.gcs_source import GCSSource
from sources.google_drive_source import GoogleDriveSource

def build_source(source_cfg: dict, table_cfg: dict):
    stype = source_cfg["type"]
    
    if stype == "gcs":
        return GCSSource(
            bucket_name=source_cfg["bucket_name"],
            object_name=table_cfg["object_name"],
            sep = table_cfg["sep"]
        )

    if stype == "google_drive":
        sep = table_cfg.get("sep", source_cfg.get("default_sep", ","))
        return GoogleDriveSource(
            file_id=table_cfg["file_id"],
            sep=sep,
        )

    raise ValueError(f"Unsupported source type: {stype}")