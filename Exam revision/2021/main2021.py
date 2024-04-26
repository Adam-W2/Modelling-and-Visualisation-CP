import matplotlib
matplotlib.use("TKAgg")
import matplotlib.pyplot as plt
from grid2021 import Grid
import pandas as pd
import numpy as np
from scipy.signal import find_peaks


#N,dx,dt,nsteps,phi_zero = input("Please input N, dx, dt number of steps and phi zero: ").split(" ")

N = 50
dx = 1
dt = 0.1
nsteps = 10000


N = int(N)
dx = float(dx)
dt = float(dt)
nsteps = int(nsteps)


which = "or"
if which == "ori":

    grid = Grid(dx,dt,N)
    grid.create_random_grid(grid.grid_a)
    grid.create_random_grid(grid.grid_b)
    grid.create_random_grid(grid.grid_c)

    animate = grid.grid_t

    alist = []
    blist = []
    clist = []
    nlist = []
    for i in range(nsteps):
        grid.steps()
        grid.update_t()
        if i % 5 == 0:

            alist.append(np.count_nonzero(grid.grid_t == 1)/N**2)
            blist.append(np.count_nonzero(grid.grid_t == 2)/N**2)
            clist.append(np.count_nonzero(grid.grid_t == 3)/N**2)
            nlist.append(i)
            plt.cla()
            im = plt.imshow(animate, animated=True)
            plt.draw()
            plt.pause(0.00001)
    plt.figure(figsize=(8,6))
    plt.plot(nlist,alist,label="A")
    plt.plot(nlist, blist,label="B")
    plt.plot(nlist, clist,label="C")
    plt.ylim(ymax=1,ymin=0)
    plt.legend()
    plt.show()
elif which == "sims":
    sims = 100
    nlist = []
    for i in range(sims):
        grid = Grid(dx,dt,N)
        grid.create_random_grid(grid.grid_a)
        grid.create_random_grid(grid.grid_b)
        grid.create_random_grid(grid.grid_c)
        flag = True
        n = 0
        while flag:
            grid.steps()
            grid.update_t()
            a = np.count_nonzero(grid.grid_t == 1)/N**2
            b = np.count_nonzero(grid.grid_t == 2)/N**2
            c = np.count_nonzero(grid.grid_t == 3)/N**2
            choice = [a,b,c]
            if max(choice) == 1:
                flag = False
            if n * dt >= 1000:
                flag = False
            n += 1

        nlist.append(n)
    mean = np.mean(nlist)
    std = np.std(nlist,ddof=1)
    n = len(nlist)
    error = std/np.sqrt(n)
    print(f"average absorption: {mean} +/- {error}")

elif which == "peaks":
    grid = Grid(dx,dt,N)
    grid.create_random_grid(grid.grid_a)
    grid.create_random_grid(grid.grid_b)
    grid.create_random_grid(grid.grid_c)

    animate = grid.grid_t

    a1list = []
    a2list = []
    nlist = []
    for i in range(nsteps):
        grid.steps()
        grid.update_t()
        a1list.append(grid.grid_a[int(N/2),int(N/3)])
        a2list.append(grid.grid_a[int(N/3),int(N/2)])
        nlist.append(i)

    peaks1, _ = find_peaks(a1list[1000:])
    peaks2, _ = find_peaks(a2list[1000:])

    peaks1_dis = np.diff(peaks1)
    peaks2_dis = np.diff(peaks2)

    period1 = np.mean(peaks1_dis)
    period2 = np.mean(peaks2_dis)

    print(period1)
    print(period2)

    plt.plot(nlist,a1list,label = "A1")
    plt.plot(nlist,a2list,label = "A2")
    plt.legend()
    plt.show()

else:
    rlist = np.arange(1,25,1)
    problist = []
    for r in rlist:
        temp = []
        for j in range(10):
            grid = Grid(dx,dt,N)
            grid.create_random_grid(grid.grid_a)
            grid.create_random_grid(grid.grid_b)
            grid.create_random_grid(grid.grid_c)
            prob = 0
            for i in range(nsteps):
                grid.steps()
                grid.update_t()
                coord1 = grid.grid_t[int(N/2),int(N/2)]
                coord2 = grid.grid_t[int(N/2 + r),int(N/2)]
                if coord1 == coord2:
                    prob += 1
            temp.append(prob/nsteps)
        problist.append(np.mean(temp))
        print(f"Distance {r} done...")

    plt.plot(rlist,problist)
    plt.show()