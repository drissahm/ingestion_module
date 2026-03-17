from sources.abstract_source import AbstractSource
from destinations.abstract_destination import AbstractDestination
         
class TableIngestionJob:
    def __init__(self, source: AbstractSource, destination: AbstractDestination):
        self.source = source
        self.destination = destination

    def run(self):
        df = self.source.read()
        self.destination.write(df)