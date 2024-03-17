from Paco_Project.Code_Fix.csv_to_sql_server import create_database_connection
from Paco_Project.Code_Fix.csv_to_sql_server import read_csv_and_print_head
from Paco_Project.Code_Fix.csv_to_sql_server import write_dataframe_to_sql


def main():
    # Database connection details
    server_name = 'DESKTOP-9PEK18E'
    database_name = 'Paco_data'
    schema_name = 'DATA'
    table_name = 'BMW'
    file_path = r'C:\Users\user\Desktop\PFE_Khairedine\Paco_Project\Data\BMW_DATA.csv'

    # Create the database connection
    engine = create_database_connection(server_name, database_name, schema_name)

    df = read_csv_and_print_head(file_path)

    # Write the DataFrame to a SQL table
    write_dataframe_to_sql(df, engine, "dbo.BMW")


if __name__ == "__main__":
    main()