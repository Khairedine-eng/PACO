from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.engine import Engine

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
        connection_string = f"mssql+pyodbc://{server_name}/{database_name}?driver=ODBC+Driver+17+for+SQL+Server&Trusted_Connection=yes&schema={schema_name}"
    else:
        connection_string = f"mssql+pyodbc://{server_name}/{database_name}?driver=ODBC+Driver+17+for+SQL+Server&Trusted_Connection=yes"

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
    metadata.reflect(bind=engine)

    if table_name in metadata.tables:
        table = metadata.tables[table_name]
        with engine.connect() as conn:
            query = table.select()
            result_proxy = conn.execute(query)
            df = pd.DataFrame(result_proxy.fetchall(), columns=result_proxy.keys())
        return df
    else:
        raise Exception(f"Table {table_name} not found in the database.")











import pandas as pd


def write_dataframe_to_sql(data_frame, engine, table_name_with_schema):
    """
    Writes the DataFrame to a SQL table.
    """
    data_frame.to_sql(name=table_name_with_schema, con=engine, if_exists='replace', index=False)

def read_csv_and_print_head(file_path):
    """
    Reads the CSV file, prints the DataFrame, and returns it.
    """
    csv_file = pd.read_csv(file_path, sep=';')
    if csv_file is not None:
        print("DataFrame:")
        print(csv_file.head())
        print("Columns:")
        print(csv_file.columns)
    return csv_file
