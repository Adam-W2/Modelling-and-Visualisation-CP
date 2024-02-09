import matplotlib
matplotlib.use("TKAgg")
import matplotlib.pyplot as plt
from Grid import Grid
import numpy as np

Choice = input("Random or Set initial? ")
if Choice == "R":
    N,P,nsteps = input("Input array size, probability and number of steps: ").split()
    nsteps = int(nsteps)
    grid = Grid(int(N),float(P))
    equilstep = []

    for i in range(1001):
        j = 0
        sumold = 0
        grid.create_random_grid()
        alivelist = []
        nstepslist = np.arange(0, nsteps, 1)

        for n in range(nsteps):
            grid.conways_game()
            sumnew = grid.summing()

            if sumnew == sumold:
                j += 1
                equil = n
            else:
                n = 0

            alivelist.append(sumnew)
            # show animation
            plt.cla()
            im = plt.imshow(grid.grid_array, animated=True, vmin=0, vmax=1)
            plt.draw()
            plt.pause(0.0001)

            if j >= 100:
                equilstep.append(equil-100)
                break

            sumold = sumnew
            if n % 10 == 0:
                print(n)
else:
    set,N,P,nsteps = input("Input set,array size,probability and number of steps: ").split()
    nsteps = int(nsteps)
    grid = Grid(int(N),float(P))

    if set == "blinker":
        grid.blinker()

    elif set == "glider":
        grid.glider()

    elif set == "toad":
        grid.toad()

    elif set == "lightship":
        grid.lightship()

    else:
        print("NOT A VALID SET")

alivelist = []
nstepslist = np.arange(0,nsteps,1)
for n in range(nsteps):
    grid.conways_game()
    alivelist.append(grid.summing())
    # show animation
    plt.cla()
    im = plt.imshow(grid.grid_array,animated=True,vmin=0,vmax=1)
    plt.draw()
    plt.pause(0.0001)
    if n % 10 == 0:
        print(n)

fig2 = plt.figure("Figure 2")
plt.plot(nstepslist,alivelist)
plt.show()