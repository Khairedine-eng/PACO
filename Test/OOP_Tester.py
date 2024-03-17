import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def plot_correlation_matrix(df):
    correlation_matrix = df.corr()

    # Plot the heatmap of the correlation matrix
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5, annot_kws={"size": 10})
    plt.title("Triangle inférieur de la matrice de corrélation")
    plt.show()
    correlation_matrix.to_csv('correlation_matrix.csv', index=False)
