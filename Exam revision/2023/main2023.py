import matplotlib
matplotlib.use("TKAgg")
import matplotlib.pyplot as plt
from grid2023 import Grid
import numpy as np
import pandas as pd

which = "dt"
if which == "det":
    nsteps = 500
    N = 100

    nsteps = int(nsteps)
    grid = Grid(int(N),0.5)
    grid.generate_pie_array()
    Rlist = []
    nlist = []
    n = 0
    for i in range(nsteps):
        if grid.grid_array[int(N/2),int(N/3)] == 0:
            Rlist.append(1)
            nlist.append(n)
        else:
            Rlist.append(0)
            nlist.append(n)
        grid.step()
        n += 1
        # show animation
        plt.cla()
        im = plt.imshow(grid.grid_array, animated=True)
        plt.draw()
        plt.pause(0.0001)

    df = pd.DataFrame({"Rvalues":Rlist,"n":nlist})
    df.to_csv("deterministicRvalue.csv",index=False)

    fig2 = plt.figure("Figure 2")
    plt.plot(nlist,Rlist)
    plt.show()

elif which == "p3":
    nsteps = 1500
    N = 50

    nsteps = int(nsteps)
    p3list = np.arange(0,0.105,0.005)
    frac = []
    for i in p3list:
        averagelist = []
        grid = Grid(int(N), i)
        grid.create_random_grid()

        for k in range(nsteps):
            grid.step_sto()
            if k % 10 == 0:
                _, counts = np.unique(grid.grid_array,return_counts=True)
                mino = np.min(counts)
                if len(counts) <= 2:
                    averagelist.append(0)
                else:
                    averagelist.append(mino/N**2)
        frac.append(sum(averagelist)/len(averagelist))
        print(f"{i} is done")

    df = pd.DataFrame({"Value of prob 3":p3list,"fraction":frac})
    df.to_csv("stochasticp3.csv",index=False)

    plt.plot(p3list,frac)
    plt.show()

else:
    nsteps = 1500
    N = 50

    nsteps = int(nsteps)
    p2list = np.linspace(0, 0.3, 10)
    p3list = np.linspace(0, 0.3, 10)

    array = np.zeros((len(p3list),len(p2list)))
    x = 0
    for i in p3list:
        y = 0
        for j in p2list:
            averagelist = []
            grid = Grid(int(N),j,i)
            grid.create_random_grid()

            for k in range(nsteps):
                grid.step_sto()
                if k % 10 == 0:
                    _, counts = np.unique(grid.grid_array, return_counts=True)
                    mino = np.min(counts)
                    if len(counts) <= 2:
                        averagelist.append(0)
                    else:
                        averagelist.append(mino / N ** 2)
            array[x][y] = sum(averagelist)/len(averagelist)
            print(f"coord {x},{y} is done")
            y +=1
        x +=1

    df = pd.DataFrame(array)
    df.to_csv("stochasticp3p2.csv", index=False)

    plt.imshow(array)
    plt.colorbar()
    plt.show()

