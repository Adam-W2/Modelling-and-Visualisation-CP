import matplotlib
matplotlib.use("TKAgg")
import matplotlib.pyplot as plt
from Grid import Grid
import pandas as pd
import numpy as np

sig,k,v,N,dt,nsteps,phi_zero = input("Please input sig, k, v, N, dt, number of steps and phi zero: ").split(" ")

N = int(N)
sig = float(sig)
k = float(k)
dt = float(dt)
nsteps = int(nsteps)
phi_zero = float(phi_zero)
v = float(v)
grid = Grid(sig,k,v,dt,phi_zero,N)
grid.create_phi_grid()
n = 0
nlist =[]
sumlist = []
grid.velocity()
print(grid.vcalc)

for i in range(nsteps):
    grid.steps_Q5()
    n += 1
    sumlist.append(grid.grid_phi.sum()/N**2)
    nlist.append(n)
    if i % 10 == 0:
        plt.cla()
        im = plt.imshow(grid.grid_phi, animated=True)
        plt.draw()
        plt.pause(0.00001)