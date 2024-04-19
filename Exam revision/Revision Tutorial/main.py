import matplotlib
matplotlib.use("TKAgg")
import matplotlib.pyplot as plt
from Grid import Grid
import pandas as pd

sig,k,N,dt,nsteps,phi_zero = input("Please input sig, k, N, dt, number of steps and phi zero: ").split(" ")

N = int(N)
sig = float(sig)
k = float(k)
dt = float(dt)
nsteps = int(nsteps)
phi_zero = float(phi_zero)

grid = Grid(sig,k,dt,phi_zero,N)
grid.create_phi_grid()

for i in range(nsteps):
    grid.steps()
    if i % 10 == 0:
        plt.cla()
        im = plt.imshow(grid.grid_phi, animated=True)
        plt.draw()
        plt.pause(0.00001)
