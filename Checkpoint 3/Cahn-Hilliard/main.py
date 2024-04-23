import matplotlib
matplotlib.use("TKAgg")
import matplotlib.pyplot as plt
from Grid import Grid
import pandas as pd
import numpy as np

N,dx,dt,nsteps,phi_zero = input("Please input N, dx, dt number of steps and phi zero: ").split(" ")

N = int(N)
dx = float(dx)
dt = float(dt)
nsteps = int(nsteps)
phi_zero = float(phi_zero)

free = []
steps = []
n = 0

grid = Grid(dx,dt,phi_zero,N)
grid.create_phi_grid()

for i in range(nsteps):
    grid.steps()
    if i % 10 == 0:
        free.append(grid.free_energy())
        steps.append(i)
        print(np.mean(grid.grid_phi))

        plt.cla()
        im = plt.imshow(grid.grid_phi, animated=True)
        plt.draw()
        plt.pause(0.00001)

    n += 1
df = pd.DataFrame({"Free energy":free,"step":steps})
df.to_csv("Data/free_energy_05_100000.csv",index=False)

fig2 = plt.figure("Figure 2")
plt.plot(steps,free)
plt.title("phizero = 0.5")
plt.show()