import matplotlib
matplotlib.use("TKAgg")
import numpy as np
import random
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from Dynamics import run_dynamics

nsteps = 1000
N, T, D = input("Input size of array, temperature and type of dynamics: ").split(" ")
X = int(N)
Y = X
kT = float(T)
spins = np.ones((X,Y))
"""""
for i in range(X):
    for j in range(Y):
        r = random.random()
        if r < 0.5: spins[i,j] = -1
        else: spins[i,j] = 1
"""""
fig = plt.figure()
im = plt.imshow(spins, animated=True)

E,M,modM,c,x = run_dynamics(nsteps,X,D,kT,spins)


print(E,M,modM,c,x)
#start temp 1, for glauber all up or down, start random is okay but get stripe. The you have to wait to get rid of sttripe. Start all up or down to calculate temp