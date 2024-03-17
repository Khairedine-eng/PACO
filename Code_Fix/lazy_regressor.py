import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from lazypredict.Supervised import LazyRegressor
from sklearn.model_selection import train_test_split

from sklearn.model_selection import train_test_split

def lazy_regressor_fit(X, y, test_size=0.2, random_state=None):
    """
    Split the data into train and test sets, create a lazy regressor model,
    fit it with the training data, and predict on the test data.

    Parameters:
    - X: The input features.
    - y: The target variable.
    - test_size: The proportion of the dataset to include in the test split.
    - random_state: Controls the shuffling applied to the data before applying the split.

    Returns:
    - reg: The trained lazy regressor model.
    - y_true: The true target values for the test set.
    - y_pred: The predicted values on the test set.
    """
    # Split the data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    # Initialize LazyRegressor
    reg = LazyRegressor(verbose=0, ignore_warnings=True, custom_metric=None)

    # Train the model
    reg.fit(X_train, y_train)

    # Predict on the test set
    y_pred = reg.predict(X_test)

    return reg, y_test, y_pred

def evaluate_model(y_test, y_pred):
    """
    Evaluate the model using various metrics.

    Parameters:
    - y_test: The true target values.
    - y_pred: The predicted target values.
    """
    # Calculate evaluation metrics
    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print("Evaluation Metrics:")
    print(f"Mean Squared Error: {mse:.2f}")
    print(f"Mean Absolute Error: {mae:.2f}")
    print(f"R-squared: {r2:.2f}")

def plot_results(y_test, y_pred):
    """
    Plot the true vs. predicted values.

    Parameters:
    - y_test: The true target values.
    - y_pred: The predicted target values.
    """
    # Plot the results
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(x=y_test, y=y_pred, ax=ax)
    ax.set_xlabel("True Values")
    ax.set_ylabel("Predictions")
    ax.set_title("True vs. Predicted Values")
    plt.show()
