import statsmodels.api as sm
from sklearn.metrics import mean_squared_error, r2_score


def train_test_sm_ols(X_train, y_train, X_test, y_test):
    # Fit the model
    model = sm.OLS(y_train, X_train)
    model_fit = model.fit()

    # Predict on the test set
    y_pred = model_fit.predict(X_test)

    # Calculate evaluation metrics
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    # Calculate mean absolute scaled error (MASE)
    abs_errors = abs(y_test - y_pred)
    mase = abs_errors.mean() / abs(y_test.diff()).mean()

    # Return model and evaluation metrics
    return model_fit, mse, r2, mase

# Example usage:
# Assuming X_train, y_train, X_test, y_test are your train and test data
# model, mse, r2, mase = train_test_sm_ols(X_train, y_train, X_test, y_test)
# print("Mean Squared Error:", mse)
# print("R-squared:", r2)
# print("Mean Absolute Scaled Error (MASE):", mase)
# print(model.summary())
