from Code_Fix.csv_to_sql_server import *

def main():

    server_name = 'DESKTOP-9PEK18E'
    database_name = 'Paco_data'
    schema_name = 'DATA'
    engine = create_database_connection(server_name, database_name, schema_name=schema_name)


    csv_file_path = r'C:\Users\user\Desktop\PFE_Khairedine\Paco_Project\Data\BMW_DATA.csv'
    df = read_csv_and_print_head(csv_file_path)

    if df is not None:
        table_name = 'BMW'
        write_dataframe_to_sql(df, engine, table_name)

if __name__ == "__main__":
    main()