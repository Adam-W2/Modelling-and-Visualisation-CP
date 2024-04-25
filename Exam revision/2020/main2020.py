import matplotlib
matplotlib.use("TKAgg")
import matplotlib.pyplot as plt
from grid2020 import Grid
import pandas as pd
import numpy as np
which = "or"
if which == "ori":
    N = 50
    P = 0.6
    nsteps = 5000

    nlist = np.arange(0,nsteps,1)
    total = []
    plist = np.arange(0.55,0.7, 0.005)
    error = []

    for p in plist:
        grid = Grid(N, p)
        grid.create_random_grid()
        temp1 = []
        temp2 = []
        for i in range(nsteps):
            grid.SIRS()
            temp1.append(np.sum(grid.grid_array))
            temp2.append(np.sum(grid.grid_array**2))

            if i % 1000 == 0:
                print(i)
        avg1 = sum(temp1)/len(temp1)
        avg2 = sum(temp2)/len(temp2)
        total.append((avg2 - avg1**2) * 1/N**2)
        error.append(grid.jacknife(temp1))
    df = pd.DataFrame({"P":plist,"Variance":total,"Error":error})
    df.to_csv("Variance_partd.csv",index=False)

    fig2 = plt.figure("Figure 2")
    plt.errorbar(plist,total,yerr=error,capsize=2, markeredgewidth=1)
    plt.title("Variance part d")
    plt.show()
else:
    N = 50
    p = 0.65
    nsteps = 300
    repeat = 200
    prob = np.zeros(nsteps)
    for j in range(repeat):
        grid = Grid(N, p)
        grid.create_one_grid()
        for i in range(nsteps):
            grid.SIRS()
            if np.sum(grid.grid_array) > 0:
                prob[i] += 1
        if j % 50 == 0:
            print(f"Finished simulation {j}...")
    probability = prob/repeat
    t = np.arange(0,300,1)
    df = pd.DataFrame({"t":t,"Probability":probability})
    df.to_csv("prob_0.6_partf.csv",index=False)

    fig2 = plt.figure("Figure 2")
    plt.loglog(t,probability)
    plt.title("prob 0.6 part f")
    plt.show()