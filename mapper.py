import sys
import numpy as np

from sklearn.metrics import mean_squared_error
from sklearn import preprocessing

import time
start = time.process_time()

X = []
Y = []
for line in sys.stdin:
    line = line.strip()
    x = line.split(',')
    x = [float(i) for i in x]
    Y.append(x[-1])
    X .append(x[:-1])

X = np.array(X, dtype=float)
Y = np.array(Y, dtype=float)


# X = np.array(x_scaled, dtype=float)
# y = np.array(y_scaled, dtype=float)


num_iterations = 25
learning_rate = 0.01
T = X.shape[0]

# print(X.shape, Y.shape)

batch_size = X.shape[0]
# batch_size = 20
batch_size = 5 if batch_size == 0 else batch_size

# print(X.shape, Y.shape, batch_size)


def training(X, Y):
    m, n = X.shape
    weights = np.zeros(n)
    b = 0
    n_samples, n_features = X.shape
    for iter in range(num_iterations):

        # for t in range(T):
        #     x = X[t]
        #     y = Y[t]
        #     y_hat = np.dot(x, weights)
        #     error = y - y_hat

        #     weights += learning_rate * (x*error)
        #     # b += learning_rate * error
        #     print(weights, learning_rate, (x*error), error)

        # y_cap = np.dot(X, weights)+b
        # weights -= learning_rate*((1/m) * np.dot(X.T, (y_cap-Y)))
        # b -= learning_rate*((1/m)*np.sum(y_cap-Y))
        # print(weights, learning_rate, np.dot(X.T, (y_cap-Y)), b, y_cap-Y)

        indices = np.random.permutation(n_samples)
        X = X[indices]
        Y = Y[indices]
        for i in range(0, n_samples, batch_size):
            X_batch = X[i:i + batch_size]
            y_batch = Y[i:i + batch_size]
            y_pred = np.dot(X_batch, weights)
            error = y_pred - y_batch
            gradients = np.dot(X_batch.T, error) / batch_size

            weights -= learning_rate * gradients
        # print("iter:", iter, " :", mean_squared_error(np.dot(X, weights), Y, squared=False))

    return weights, b


weights, b = training(X, Y)


for i in range(weights.shape[0]):
    print('%s\t%s' % (i, weights[i]))

print('%s\t%s' % (weights.shape[0], b))

# weights = list(round(i, 3) for i in weights)
# b = round(b, 3)
# print(weights, b)
# print to stderr
print(time.process_time() - start, file=sys.stderr)
# print rmse
print(mean_squared_error(np.dot(X, weights), Y, squared=False))
