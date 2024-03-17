from sklearn.metrics import mean_squared_error, r2_score
from statsmodels.tsa.stattools import acovf
import numpy as np

def mean_absolute_scaled_error(y_true, y_pred, y_train):
    """
    Calculate Mean Absolute Scaled Error (MASE).

    Parameters:
    - y_true (array-like): True values.
    - y_pred (array-like): Predicted values.
    - y_train (array-like): Training data.

    Returns:
    - mase (float): Mean Absolute Scaled Error.
    """
    scale = acovf(y_train)
    errors = y_true - y_pred
    mae = np.mean(np.abs(errors))
    mase = mae / np.mean(np.abs(scale))
    return mase

from statsmodels.tsa.statespace.sarimax import SARIMAX

from statsmodels.tsa.statespace.sarimax import SARIMAX

def train_test_sarimax(X_train, X_test, y_train, y_test, order=(1, 1, 1), seasonal_order=(0, 0, 0, 0)):
    """
    Train and test SARIMAX model.

    Args:
        X_train (DataFrame): Exogenous variables training data.
        X_test (DataFrame): Exogenous variables testing data.
        y_train (Series): Target variable training data.
        y_test (Series): Target variable testing data.
        order (tuple): Non-seasonal ARIMA order.
        seasonal_order (tuple): Seasonal ARIMA order.

    Returns:
        float, float, float, Series: Mean squared error, R-squared score, mean absolute scaled error, predictions.
    """
    # Preprocess exogenous variables
    X_train = preprocess_exog(X_train)
    X_test = preprocess_exog(X_test)

    # Train SARIMAX model
    model = SARIMAX(endog=y_train, exog=X_train, order=order, seasonal_order=seasonal_order)
    fitted_model = model.fit()

    # Make predictions
    predictions = fitted_model.forecast(steps=len(X_test), exog=X_test)

    # Evaluate model
    mse = mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)
    mase = mean_absolute_scaled_error(y_test, predictions)

    return mse, r2, mase, predictions

def preprocess_exog(X):
    """
    Preprocess exogenous variables.

    Args:
        X (DataFrame): Exogenous variables.

    Returns:
        DataFrame: Preprocessed exogenous variables.
    """
    # Fill missing values with 0
    X.fillna(0, inplace=True)

    # Identify columns with string values
    str_cols = X.select_dtypes(include=['object']).columns

    # Convert string columns to numeric type
    X[str_cols] = X[str_cols].apply(lambda x: x.str.replace(',', '.').astype(float))


    return X

