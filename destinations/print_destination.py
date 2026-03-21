from destinations.abstract_destination import AbstractDestination
import pandas as pd

class PrintDestination(AbstractDestination):
    
    def write(self, df: pd.DataFrame):
        print(df.to_string(index=False))