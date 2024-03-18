from sklearn.model_selection import train_test_split
from Paco_Project.Test.Sarimax.ARIMAX import fit_sarimax
def split_data(X, y, test_size=0.2, random_state=None):
    """
    Split the data into training and testing sets.

    Args:
        X (DataFrame): Exogenous variables.
        y (Series): Target variable.
        test_size (float): The proportion of the dataset to include in the test split (default is 0.2).
        random_state (int): Random seed for reproducibility (default is None).

    Returns:
        DataFrame, DataFrame, Series, Series: X_train, X_test, y_train, y_test.
    """
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    return X_train, X_test, y_train, y_test


from Paco_Project.Code_Fix.csv_to_sql_server import create_database_connection
from Paco_Project.Code_Fix.csv_to_sql_server import fetch_table_data
from Paco_Project.Code_Fix.Data_Processing import retrieve_data
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, mean_squared_error



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

            filtered_df['Date'] = pd.to_datetime(filtered_df['Date'], format='%d/%m/%Y')

            # Convert numeric columns to float and replace commas with periods
            numeric_cols = ['NH Budget', 'NH Actual', 'Production Calendar', 'Customer Calendar', 'ADC Calendar',
                            'Customer Consumption Last 12 week', 'Stock Plant : TIC Tool', 'CLIENT FORCAST S1',
                            'HC DIRECT', 'HC INDIRECT', 'ABS P', 'ABS NP', 'FLUCTUATION']

            filtered_df[numeric_cols] = filtered_df[numeric_cols].replace(',', '.', regex=True).astype(float)

            # Separate target variable (y)
            y = filtered_df['NH Actual'].replace(',', '.', regex=True).astype(float)

            # Select exogenous variables (X)
            X = filtered_df.drop(columns=['NH Actual', 'Date'])

            # Fill missing values with 0
            X.fillna(0, inplace=True)

            # Convert X and y to Pandas DataFrames
            X = pd.DataFrame(X)
            y = pd.DataFrame(y)



            # Verify the data types of X and y
            print("Data types of X and y after conversion:")
            print(X.dtypes)
            print(y.dtypes)
            print(X.describe())
            print(y.describe())
            print(X.head())
            print(y.head())

            X_train, X_test, y_train, y_test = split_data(X, y, test_size=0.2)

            X_test.reset_index(drop=True, inplace=True)
            y_test.reset_index(drop=True, inplace=True)

            model = fit_sarimax(X_train, y_train, order=(1, 0, 1), seasonal_order=(0, 0, 0, 0))

            # Debugging the issue with predictions
            print("X_test index:", X_test.index)
            print("y_test index:", y_test.index)
            print("X_test columns:", X_test.columns)



            y_pred = model.predict(X_test)
            print("y_pred columns:", y_pred)


if __name__ == "__main__":
    main()