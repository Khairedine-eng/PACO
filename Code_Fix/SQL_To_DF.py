from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.engine import Engine
import pandas as pd

def create_database_connection(server_name: str, database_name: str, schema_name: str = None) -> Engine:
    """
    Create a connection to the SQL Server database.

    Args:
        server_name (str): The name of the SQL Server instance.
        database_name (str): The name of the database.
        schema_name (str): The name of the schema (optional).

    Returns:
        Engine: SQLAlchemy engine object.
    """
    if schema_name:
        connection_string = f"mssql+pyodbc://{server_name}/{database_name}?driver=ODBC+Driver+17+for+SQL+Server&Trusted_Connection=yes"
    else:
        connection_string = f"mssql+pyodbc://{server_name}/{database_name}?driver=ODBC+Driver+17+for+SQL+Server&Trusted_Connection=yes&schema={schema_name}"

    engine = create_engine(connection_string, echo=True)
    return engine

def fetch_table_data(engine: Engine, table_name: str):
    """
    Fetch all data from the specified table.

    Args:
        engine (Engine): SQLAlchemy engine object.
        table_name (str): Name of the table from which to fetch data.
    """
    metadata = MetaData()
    table = Table(table_name, metadata, autoload=True, autoload_with=engine)

    with engine.connect() as conn:
        query = table.select()
        result_proxy = conn.execute(query)
        df = pd.DataFrame(result_proxy.fetchall(), columns=result_proxy.keys())
    return df


