import matplotlib
matplotlib.use("TKAgg")
import matplotlib.pyplot as plt
from Grid import Grid
import pandas as pd
import numpy as np

sig,k,N,dt,nsteps,phi_zero = input("Please input sig, k, N, dt, number of steps and phi zero: ").split(" ")

N = int(N)
sig = float(sig)
k = float(k)
dt = float(dt)
nsteps = int(nsteps)
phi_zero = float(phi_zero)
v = 1

grid = Grid(sig,k,v,dt,phi_zero,N)
grid.create_phi_grid()
n = 0
nlist =[]
sumlist = []

for i in range(nsteps):
    grid.steps()
    n += 1
    sumlist.append(grid.grid_phi.sum()/N**2)
    nlist.append(n)
    if i % 10 == 0:
        plt.cla()
        im = plt.imshow(grid.grid_phi, animated=True)
        plt.draw()
        plt.pause(0.00001)

center_point = np.array((int(grid.grid_phi.shape[0] / 2.), int(grid.grid_phi.shape[1] / 2.)))
points = np.argwhere(grid.grid_phi <= 1000)
rsquare = ((points - center_point)**2).sum(axis=1).reshape((grid.rows,grid.columns))

rlist = []
philist = []
for i in range(np.max(rsquare)):
    rlist.append(i)
    position = np.argwhere(rsquare == i)
    if len(position) > 0:
        print(grid.grid_phi[position])
        philist.append(sum(grid.grid_phi[position])/len(position))
    else:
        philist.append(0)


df2 = pd.DataFrame(grid.grid_phi)
df2.to_csv("grid.csv")

df1 = pd.DataFrame({"Phi":philist,"Distance":rlist})
df1.to_csv("Philist.csv",index=False)

fig2 = plt.figure("Figure 2")
plt.plot(rlist,philist)
plt.title("Sumlist")
plt.show()

df = pd.DataFrame({"Sum":sumlist,"step":nlist})
df.to_csv("sumlist.csv",index=False)

fig3 = plt.figure("Figure 3")
plt.plot(nlist,sumlist)
plt.title("Sumlist")
plt.show()