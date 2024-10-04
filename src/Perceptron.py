import numpy as np

class Perceptron:

    def __init__(self, learning_rate = 0.01, n_iters = 1000):
        self.lr = learning_rate
        self.n_iters = n_iters
        self.activation_func = self._unit_step_func
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0
        y_ = np.array([1 if i > 0.5 else 0 for i in y])

        for _ in range(self.n_iters):
            for idx, x_i in enumerate(X):
                linear_output = np.dot(x_i, self.weights) + self.bias
                y_pred = self.activation_function(linear_output)
                update = self.lr * (y_[idx] - y_pred)
                self.weights += update * x_i
                self.bias += update


    def _predict(self, X):
        linear_output = np.dot(X, self.weights) + self.bias
        y_pred = self.activation_function(linear_output)
        return y_pred

    def _unit_step_func(self, x):
        return np.where(x >= 0.5, 1, 0)
