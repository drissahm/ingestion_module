from pipeline.ingestion_job import IngestionJob
from sources.google_drive_source import GoogleDriveSource
from destinations.print_destination import PrintDestination
from destinations.bigquery_destination import BigQueryDestination


source = GoogleDriveSource("1PGuUkYTSjOSIjIv_qi3ga6lsH8Sz7bxn", sep = ";")
dest =  BigQueryDestination("african-tech-skills-c295", "03_gold", "test_ingestion_gdrive")

job = IngestionJob(source, dest)
job.run()