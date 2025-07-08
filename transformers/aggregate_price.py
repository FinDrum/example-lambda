import pandas as pd

import logging

logger = logging.getLogger("findrum")

from findrum.interfaces import Operator

class AggregatePrices(Operator):
    def run(self, input_data):
        df = input_data.copy()
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df['hour'] = df['timestamp'].dt.floor('h')

        result = df.groupby(['symbol', 'hour']).agg({
            'close': 'mean',
        }).reset_index()

        result.rename(columns={'close': 'avg_close'}, inplace=True)
        return result