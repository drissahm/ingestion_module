from pipeline.source_factory import build_source
from pipeline.destination_factory import build_destination
from pipeline.config_loader import load_config
from pipeline.ingestion_job import IngestionJob

def run_from_config(config_path: str = "config.yaml") -> None:
    cfg = load_config(config_path)
    destination_cfg = cfg["destination"]

    for source_cfg in cfg["sources"]:
        for table_cfg in source_cfg["tables"]:
            source = build_source(source_cfg, table_cfg)
            destination = build_destination(destination_cfg, table_cfg)
            print(table_cfg)

            job = IngestionJob(source, destination)
            job.run()