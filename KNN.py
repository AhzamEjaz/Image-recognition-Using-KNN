import numpy as np

class KNN:
    def __init__(self, k):
        print(k)
        self.k = k
    def fit(self, X, y):
        self.X_train = X
        self.y_train = y
    def predict(self, X):
        predictions = [self._predict(x) for x in X]
        return predictions
    def _predict(self, x):
        distances = [self.cal_distance(x, x_train) for x_train in self.X_train]
        print(distances)

    def cal_distance(x1, x2):
        distance = np.sqrt(np.sum((x1-x2)**2))
        return distance