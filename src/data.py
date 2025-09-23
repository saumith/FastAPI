import numpy as np
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split

def load_data():
    """
    Load the Wine dataset and return all 13 features and target values.
    Returns:
        X (numpy.ndarray): Shape (n_samples, 13)
        y (numpy.ndarray): Target labels (0, 1, 2)
    """
    wine = load_wine()
    X = wine.data   # all 13 features
    y = wine.target
    return X, y

def split_data(X, y):
    """
    Split the data into training and testing sets.
    Args:
        X (numpy.ndarray): The features of the dataset.
        y (numpy.ndarray): The target values of the dataset.
    Returns:
        X_train, X_test, y_train, y_test (tuple): The split dataset.
    """
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=12, stratify=y
    )
    return X_train, X_test, y_train, y_test
