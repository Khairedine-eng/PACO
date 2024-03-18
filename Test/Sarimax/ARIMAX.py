import pandas as pd
import statsmodels.api as sm

def fit_sarimax(X, y, order=(1, 0, 1), seasonal_order=(0, 0, 0, 0), exog=None):
    """
    Fit a SARIMAX model.

    Parameters:
    - X: Exogenous variables (array-like or DataFrame).
    - y: Endogenous variable (array-like or DataFrame).
    - order: The (p,d,q) order of the non-seasonal component of the ARIMA model. Default is (1, 0, 1).
    - seasonal_order: The (P,D,Q,s) order of the seasonal component of the ARIMA model.
                      Default is (0, 0, 0, 0) indicating no seasonal effect.
    - exog: Exogenous variables (array-like or DataFrame). Default is None.

    Returns:
    - sarimax_model: Fitted SARIMAX model.
    """

    # Ensure inputs are pandas DataFrame
    if not isinstance(X, pd.DataFrame):
        X = pd.DataFrame(X)
    if not isinstance(y, pd.Series):
        y = pd.Series(y.squeeze())

    # Fit SARIMAX model
    sarimax_model = sm.tsa.SARIMAX(y, exog=exog, order=order, seasonal_order=seasonal_order, enforce_stationarity=False)
    fitted_model = sarimax_model.fit()

    return fitted_model


def predict_sarimax(model, X_future):
    """
    Make predictions with SARIMAX model.

    Parameters:
    - model: Fitted SARIMAX model.
    - X_future: Future exogenous variables (array-like).

    Returns:
    - y_pred: Predicted values.
    """
    # Predictions
    y_pred = model.predict(exog=X_future)
    return y_pred


from datetime import datetime

def get_input():
    """
    Get input from the client for future prediction.

    Returns:
    - data_for_prediction: List of data for prediction.
    """
    print("Please enter the values for the following features:")

    # Get input for each feature
    NH_Budget = float(input("NH Budget: "))
    Production_Calendar = float(input("Production Calendar: "))
    Customer_Calendar = float(input("Customer Calendar: "))
    ADC_Calendar = float(input("ADC Calendar: "))
    Customer_Consumption_Last_12_week = float(input("Customer Consumption Last 12 week: "))
    Stock_Plant_TIC_Tool = float(input("Stock Plant : TIC Tool: "))
    CLIENT_FORCAST_S1 = float(input("CLIENT FORCAST S1: "))
    HC_DIRECT = float(input("HC DIRECT: "))
    HC_INDIRECT = float(input("HC INDIRECT: "))
    ABS_P = float(input("ABS P: "))
    ABS_NP = float(input("ABS NP: "))
    FLUCTUATION = float(input("FLUCTUATION: "))
    WeekNumber = int(input("WeekNumber: "))
    Month = int(input("Month: "))
    Year = int(input("Year: "))

    # Get date input
    Date = datetime(Year, Month, WeekNumber * 7)

    # Construct list of data for prediction
    data_for_prediction = [
        NH_Budget, Production_Calendar, Customer_Calendar, ADC_Calendar,
        Customer_Consumption_Last_12_week, Stock_Plant_TIC_Tool, CLIENT_FORCAST_S1,
        HC_DIRECT, HC_INDIRECT, ABS_P, ABS_NP, FLUCTUATION, WeekNumber, Month, Year, Date
    ]

    return data_for_prediction


