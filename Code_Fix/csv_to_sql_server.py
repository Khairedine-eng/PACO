import pandas as pd
from sqlalchemy import create_engine

def create_database_connection(server_name, database_name, driver='ODBC Driver 17 for SQL Server', trusted_connection='yes', schema_name='DATA'):
    """
    Creates a connection string and returns a SQLAlchemy engine.
    """
    connection_string = (f"mssql+pyodbc://{server_name}/{database_name}"
                         f"?driver={driver}&trusted_connection={trusted_connection}"
                         f"&schema={schema_name}")
    engine = create_engine(connection_string)
    return engine

def read_csv_and_print_head(file_path):
    """
    Reads the CSV file, prints the DataFrame, and returns it.
    """
    df = pd.read_csv(file_path, sep=';')
    if df is not None:
        print("DataFrame:")
        print(df.head())
        print("Columns:")
        print(df.columns)
    return df


def write_dataframe_to_sql(df, engine, table_name):
    """
    Writes the DataFrame into SQL Server and prints a message if successful.
    """
    print("Inside write_dataframe_to_sql function")  # Debugging line
    if df is not None:
        df.to_sql(
            name=table_name,
            con=engine,
            if_exists='append',
            index=False
        )
        print("DataFrame has been successfully written to SQL Server.")


