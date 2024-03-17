import matplotlib.pyplot as plt

def plot_train_test_predictions(ytrain, ytest, predictions):
    """
    Plot training and testing data along with predictions.

    Parameters:
    - ytrain (pandas Series or DataFrame): Training target data.
    - ytest (pandas Series or DataFrame): Testing target data.
    - predictions (pandas Series): Predictions made by the model.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(ytrain.index, ytrain, label='Training Data', color='blue')
    plt.plot(ytest.index, ytest, label='Testing Data', color='green')
    plt.plot(ytest.index, predictions, label='Predictions', color='red')
    plt.title('SARIMAX Model: Training, Testing Data, and Predictions')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True)
    plt.show()
