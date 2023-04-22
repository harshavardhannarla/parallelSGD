

import numpy as np
import sys


weights = []

for line in sys.stdin:
    line = line.strip()
    key, val = line.split()
    weights.append((int(key), float(val)))

weights = sorted(weights, key=lambda x: x[0])
wt = [i[1] for i in weights]
wt = np.array(wt)


f = open('input.txt', 'r')
X = []
Y = []
for line in f:
    line = line.strip()
    x = line.split(',')
    x = [float(i) for i in x]
    y = x[-1]
    x = x[:-1]
    X.append(x)
    Y.append(y)

X = np.array(X, dtype=float)
Y = np.array(Y, dtype=float)
print(X.shape, Y.shape, wt.shape)

# cal rmse
y_hat = np.dot(X, wt)
rmse = np.sqrt(np.mean((y_hat - Y)**2))
print(rmse)
