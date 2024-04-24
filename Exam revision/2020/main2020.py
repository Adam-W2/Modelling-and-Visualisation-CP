import matplotlib
matplotlib.use("TKAgg")
import matplotlib.pyplot as plt
from grid2020 import Grid
import pandas as pd
import numpy as np

N = 50
P = 0.6
nsteps = 5000


grid = Grid(N,P)
grid.create_random_grid()

nlist = np.arange(0,nsteps,1)
total = []

for i in range(nsteps):
    grid.SIRS()
    total.append(np.sum(grid.grid_array)/N**2)

    if i % 1000 == 0:
        print(i)

plt.plot(nlist,total)
plt.show()