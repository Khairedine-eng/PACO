from Code_Fix.csv_to_sql_server import *
from Code_Fix.Data_Processing import *

def main():
    # Database connection details
    server_name = 'DESKTOP-9PEK18E'
    database_name = 'Paco_data'
    schema_name = 'DATA'
    driver = 'ODBC Driver 17 for SQL Server'

    connection_string = f"mssql+pyodbc://{server_name}/{database_name}?driver={{{driver}}};Trusted_Connection=yes"

    # Establish database connection
    engine = create_database_connection(server_name, database_name, schema_name=schema_name)

    # Read data from CSV file
    csv_file_path = r'C:\Users\user\Desktop\PFE_Khairedine\Paco_Project\Data\BMW_DATA.csv'
    df = read_csv_and_print_head(csv_file_path)

    # Write dataframe to SQL Server table
    if df is not None:
        table_name = 'BMW'
        write_dataframe_to_sql(df, connection_string, 'BMW')

        # Retrieve and process data from SQL Server
        df = retrieve_data(server_name, database_name, schema_name, table_name)
        if df is not None:
            print(df.info())
            print(df.describe())

if __name__ == "__main__":
    main()
