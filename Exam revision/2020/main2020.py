import matplotlib
matplotlib.use("TKAgg")
import matplotlib.pyplot as plt
from grid2020 import Grid
import pandas as pd
import numpy as np

N = 50
P = 0.7
nsteps = 5000


grid = Grid(N,P)
grid.create_random_grid()

for i in range(nsteps):
    grid.SIRS()
    if i % 10 == 0:
        plt.cla()
        im = plt.imshow(grid.grid_array, animated=True)
        plt.draw()
        plt.pause(0.00001)