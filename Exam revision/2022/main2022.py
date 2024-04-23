import matplotlib
matplotlib.use("TKAgg")
import matplotlib.pyplot as plt
from grid2022 import Grid
import pandas as pd
import numpy as np

#N,dx,dt,nsteps,phi_zero = input("Please input N, dx, dt number of steps and phi zero: ").split(" ")

N = 50
dx = 1
dt = 0.21
nsteps = 15000
phi_zero = 0.5


N = int(N)
dx = float(dx)
dt = float(dt)
nsteps = int(nsteps)
phi_zero = float(phi_zero)

which = "or"
if which == "ori":

    grid = Grid(dx,dt,phi_zero,N)
    grid.create_phi_grid()
    grid.create_M_grid()

    animate = grid.grid_phi

    Mmean = []
    phimean = []
    nlist = []

    for i in range(nsteps):
        grid.steps()
        if i % 10 == 0:
            Mmean.append(np.mean(grid.grid_M))
            print(np.mean(grid.grid_phi))
            phimean.append(np.mean(grid.grid_phi))
            nlist.append(i)
            plt.cla()
            im = plt.imshow(animate, animated=True)
            plt.draw()
            plt.pause(0.00001)

    df = pd.DataFrame({"N step":nlist,"M means":Mmean,"Phi means":phimean})
    df.to_csv("averages_partc_iii.csv",index=False)

    fig2 = plt.figure("Figure 2")
    plt.plot(nlist,Mmean)
    plt.title("M averages")

    fig3 = plt.figure("Figure 3")
    plt.plot(nlist,phimean)
    plt.title("Phi mean")

    plt.show()
else:

    alphalist = np.arange(0.0005,0.0055,0.0005)
    variance = []
    mean = []
    for i in alphalist:

        grid = Grid(dx, dt, phi_zero, N,i)
        grid.create_phi_grid()
        grid.create_M_grid()

        animate = grid.grid_phi

        Mmean = []
        Mvariance = []

        for j in range(nsteps):
            grid.steps_new()
            if j % 10 == 0:

                Mmean.append(np.mean(grid.grid_M))
                Mvariance.append(np.mean(grid.grid_M**2) - np.mean(grid.grid_M)**2)

        variance.append(np.mean(Mvariance))
        mean.append(np.mean(Mmean))
        print(f"{i} done")

    df = pd.DataFrame({"Alpha List": alphalist, "M means": mean, "M variance": variance})
    df.to_csv("variance_parte.csv", index=False)

    fig2 = plt.figure("Figure 2")
    plt.plot(alphalist, mean)
    plt.title("M averages")

    fig3 = plt.figure("Figure 3")
    plt.plot(alphalist, variance)
    plt.title("M variance")

    plt.show()