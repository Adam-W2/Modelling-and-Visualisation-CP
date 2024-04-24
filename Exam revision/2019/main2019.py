import matplotlib
matplotlib.use("TKAgg")
import matplotlib.pyplot as plt
from grid2019 import Grid
import pandas as pd
import numpy as np

which = "an"
if which == "ani":

    N = 100
    dx = 1
    dt = 0.01
    nsteps = 100000
    F = 0.035

    grid = Grid(dx, dt, N,F)
    grid.create_U_grid()
    grid.create_V_grid()
    for i in range(nsteps):
        grid.steps()
        if i % 10 == 0:
            plt.cla()
            im = plt.imshow(grid.grid_U, animated=True)
            plt.draw()
            plt.pause(0.00001)
else:

    N = 50
    dx = 1
    dt = 0.01
    nsteps = 100000
    F = np.arange(0.020,0.055,0.005)
    variance = []
    for k in F:
        temp_var = []
        grid = Grid(dx, dt, N, k)
        grid.create_U_grid()
        grid.create_V_grid()
        for i in range(nsteps):
            grid.steps()
            #temp_var.append(np.mean(grid.grid_U**2) - np.mean(grid.grid_U)**2)

        #variance.append(np.mean(temp_var))
        variance.append(np.mean(grid.grid_U**2) - np.mean(grid.grid_U)**2)
        #plt.plot(np.linspace(0,100000,100000),temp_var)
        #plt.show()
        print(f"Done F = {k}")

    df = pd.DataFrame({"F list":F,"Variance":variance})
    df.to_csv("variance_partb.csv",index=False)

    fig2 = plt.figure("Figure 2")
    plt.plot(F,variance)
    plt.title("Variance")
    plt.show()

