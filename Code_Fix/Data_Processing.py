import pandas as pd
import pyodbc

def create_database_connection(server_name, database_name, schema_name=None):
    if schema_name:
        conn_str = f'DRIVER={{SQL Server}};SERVER={server_name};DATABASE={database_name};SCHEMA={schema_name};Trusted_Connection=yes;'
    else:
        conn_str = f'DRIVER={{SQL Server}};SERVER={server_name};DATABASE={database_name};Trusted_Connection=yes;'
    return pyodbc.connect(conn_str)

def retrieve_data(server_name, database_name, schema_name, table_name):
    try:
        # Establish database connection
        engine = create_database_connection(server_name, database_name, schema_name=schema_name)

        # SQL Query to retrieve your data
        query = f"SELECT * FROM {table_name}"

        # Retrieve data into a DataFrame
        df = pd.read_sql(query, engine)

        # Close the connection
        engine.close()

        # Convert 'Date' column to datetime
        df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')

        # Extract additional date-related features
        df['WeekNumber'] = df['Date'].dt.isocalendar().week
        df['Month'] = df['Date'].dt.month
        df['Year'] = df['Date'].dt.isocalendar().year

        # Filter data for years 2022 and 2023
        df = df[(df['Year'] == 2022) | (df['Year'] == 2023)]

        # Drop unnecessary columns
        columns_to_drop = ['Sales Bud', 'Sales Act ', ' Sales Actual/Budget', 'NH Actual/Budget', 'Efficiency Bud ','Efficiency Act', 'Efficiency Actual/Budget']
        df.drop(columns=columns_to_drop, inplace=True)

        return df

    except pyodbc.Error as e:
        print("Error connecting to database:", e)
        return None


