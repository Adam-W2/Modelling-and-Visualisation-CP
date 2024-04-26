import matplotlib
matplotlib.use("TKAgg")
import matplotlib.pyplot as plt
from grid2018 import Grid
import pandas as pd
import numpy as np
from scipy.signal import find_peaks


#N,dx,dt,nsteps,phi_zero = input("Please input N, dx, dt number of steps and phi zero: ").split(" ")

X = 1000
Y = 1
dx = 1
dt = 0.09
nsteps = 10000


dx = float(dx)
dt = float(dt)
nsteps = int(nsteps)
R = 10

which = "or"
if which == "ori":

    grid = Grid(dx,dt,X,Y,R)
    grid.create_mu_grid()

    for i in range(nsteps):
        grid.steps()
        if i % 5 == 0:
            plt.cla()
            im = plt.imshow(grid.grid_mu, animated=True)
            plt.draw()
            plt.pause(0.00001)
else:
    grid = Grid(dx,dt,X,Y,R)
    grid.create_mu_grid_1D()

    for i in range(nsteps):
        grid.steps_1D()
        if i % 5 == 0:
            plt.cla()
            im = plt.imshow(grid.grid_mu, animated=True)
            plt.draw()
            plt.pause(0.00001)