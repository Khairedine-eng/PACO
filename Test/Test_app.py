from Paco_Project.Code_Fix.csv_to_sql_server import create_database_connection
from Paco_Project.Code_Fix.csv_to_sql_server import fetch_table_data
from Paco_Project.Code_Fix.Data_Preparation import *
from Paco_Project.Code_Fix.Data_Processing import retrieve_data



def main():
    # Database connection details
    server_name = 'DESKTOP-9PEK18E'
    database_name = 'Paco_data'
    schema_name = 'DATA'
    table_name = 'BMW'

    # Create the database connection
    engine = create_database_connection(server_name, database_name, schema_name)

    # Fetch all data from the "BMW" table
    df = fetch_table_data(engine, table_name)

    if df is not None:
        print(df)
        print(df.info())
        print(df.describe())

        raw_df = retrieve_data(df)

        if raw_df is not None:
            # Specify years to filter
            years_to_filter = [2022, 2023]  # Add more years as needed

            # Filter data for specified years
            filtered_df = raw_df[raw_df['Year'].isin(years_to_filter)]

            # Drop unnecessary columns
            columns_to_drop = ['Sales Bud', 'Sales Act ', ' Sales Actual/Budget', 'NH Actual/Budget', 'Efficiency Bud ',
                                   'Efficiency Act', 'Efficiency Actual/Budget']
            filtered_df.drop(columns=columns_to_drop, inplace=True)

            # Further processing or analysis can be done here

            print(filtered_df.head())

            # Prepare data for modeling
            X, y = prepare_data_for_modeling(filtered_df)

            # Example: Print X and y
            print("Exogenous Variables (X):")
            print(X)
            print("\nTarget Variable (y):")
            print(y)

            X_train, X_test, y_train, y_test = split_data(X, y, test_size=0.2, random_state=42)

            # Example: Print the shapes of train and test sets
            print("Train set shapes:")
            print("X_train:", X_train.shape)
            print("y_train:", y_train.shape)
            print("\nTest set shapes:")
            print("X_test:", X_test.shape)
            print("y_test:", y_test.shape)



if __name__ == "__main__":
    main()