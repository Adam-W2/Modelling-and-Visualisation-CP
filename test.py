import matplotlib.pyplot as plt
import numpy as np
import random

X = 50
Y = X
spins = np.zeros((X,Y))

for i in range(X):
    for j in range(Y):
        r = random.random()
        if r < 0.5: spins[i,j] = -1
        else: spins[i,j] = 1

print(-1 % 50)