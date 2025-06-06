from sqlalchemy import create_engine

from findrum.interfaces import Operator

class PostgresWriter(Operator):
    def __init__(self, table, db_url="postgresql://postgres:yourpass@localhost:5432/stockdb"):
        self.table = table
        self.db_url = db_url

    def run(self, input_data):
        engine = create_engine(self.db_url)
        input_data.to_sql(self.table, engine, if_exists='append', index=False)
        return input_data

