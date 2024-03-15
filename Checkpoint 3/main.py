import matplotlib
matplotlib.use("TKAgg")
import matplotlib.pyplot as plt
from Grid import Grid
import numpy as np
import pandas as pd

N = 100
dx = 1
dt = 1
nsteps = 10000
phi_zero = 0

free = []
steps = []
n = 0

grid = Grid(dx,dt,phi_zero,N)
grid.create_phi_grid()

for i in range(nsteps):
    grid.steps()
    # show animation
    if i % 10 == 0:
        free.append(grid.free_energy())
        steps.append(i)
        plt.cla()
        im = plt.imshow(grid.grid_phi, animated=True)
        plt.draw()
        plt.pause(0.00001)
    n += 1
df = pd.DataFrame({"Free energy":free,"step":steps})
df.to_csv("Data/test1.csv",index=False)

fig2 = plt.figure("Figure 2")
plt.plot(steps,free)
plt.show()