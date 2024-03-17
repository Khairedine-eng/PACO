from sklearn.model_selection import train_test_split
import pandas as pd


def prepare_data_for_modeling(filtered_df):
    """
    Prepare the filtered DataFrame for modeling with VAR.

    Args:
        filtered_df (DataFrame): Filtered DataFrame containing the data.

    Returns:
        DataFrame, Series: X (exogenous variables), y (target variable).
    """
    # Convert 'Date' column to datetime
    filtered_df['Date'] = pd.to_datetime(filtered_df['Date'], format='%d/%m/%Y')

    # Convert numeric columns to float and replace commas with periods
    numeric_cols = ['NH Budget', 'NH Actual',
                    'CLIENT FORCAST S1', 'HC DIRECT', 'HC INDIRECT', 'ABS P', 'ABS NP', 'FLUCTUATION']
    filtered_df[numeric_cols] = filtered_df[numeric_cols].replace(',', '.', regex=True).astype(float)

    # Separate target variable (y)
    y = filtered_df['NH Actual']

    # Select exogenous variables (X)
    X = filtered_df.drop(columns=['NH Actual'])  # Drop target variable from X

    # Fill missing values with 0
    X.fillna(0, inplace=True)

    # Convert DataFrame X to numeric data types
    X = X.apply(pd.to_numeric, errors='coerce')

    return X, y

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
