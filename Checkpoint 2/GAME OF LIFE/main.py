import matplotlib
matplotlib.use("TKAgg")
import matplotlib.pyplot as plt
from Grid import Grid
import numpy as np
import pandas as pd

Choice = input("Random or Set initial? ")
if Choice == "R":
    choice2 = input("Animation or Measurement? ")
    if choice2 == "M":
        N,P,nsteps = input("Input array size, probability and number of steps: ").split()

        nsteps = int(nsteps)
        grid = Grid(int(N),float(P))
        equilstep = []
        nstepslist = np.arange(0, nsteps, 1)

        for i in range(500):
            j = 0
            sumold = 0
            grid.create_random_grid()
            alivelist = []
            print(f"Running simulation {i+1}...")
            run = True
            n = 0

            while run:
                grid.conways_game()
                sumnew = grid.summing()

                if sumnew == sumold:
                    j += 1
                    equil = n
                else:
                    j = 0

                alivelist.append(sumnew)

                n += 1
                sumold = sumnew

                if j >= 10:
                    print(f"Simulation took {equil - 100} steps!")
                    equilstep.append(equil-100)
                    run = False
                elif n == nsteps - 1:
                    print(f"Simulation reached maximum step!")
                    equilstep.append(nsteps)
                    run = False

        print("Complete!")
        df = pd.DataFrame({"nsteps":equilstep})
        df.to_csv("test2.csv")

    else:

        N,P,nsteps = input("Input array size, probability and number of steps: ").split()
        nsteps = int(nsteps)
        grid = Grid(int(N),float(P))
        grid.create_random_grid()
        alivelist = []
        nstepslist = np.arange(0, nsteps, 1)

        for n in range(nsteps):
            grid.conways_game()
            alivelist.append(grid.summing())
            # show animation
            plt.cla()
            im = plt.imshow(grid.grid_array, animated=True, vmin=0, vmax=1)
            plt.draw()
            plt.pause(0.0001)

        fig2 = plt.figure("Figure 2")
        plt.plot(nstepslist, alivelist)
        plt.show()

else:
    set,N,P,nsteps = input("Input set,array size,probability and number of steps: ").split()
    nsteps = int(nsteps)
    grid = Grid(int(N),float(P))

    if set == "blinker":
        grid.blinker()

    elif set == "glider":
        grid.glider()
        alivelist = []
        nstepslist = []
        xlist = []
        ylist = []

        for n in range(nsteps):
            grid.conways_game()
            if n % 4 == 0:
                x, y = grid.momentum()
                if x != 0 and y != 0:
                    xlist.append(x)
                    ylist.append(y)
                    nstepslist.append(n)

            alivelist.append(grid.summing())

            # show animation
            plt.cla()
            im = plt.imshow(grid.grid_array, animated=True, vmin=0, vmax=1)
            plt.draw()
            plt.pause(0.0001)

        xtruncated = []
        nsteptruncated = []
        for i in range(len(nstepslist)):
            if nstepslist[i] <= 80:
                xtruncated.append(xlist[i])
                nsteptruncated.append(nstepslist[i])

        fig1 = plt.figure("Figure 1")
        plt.plot(nstepslist, xlist)
        plt.xlabel("Time step")
        plt.ylabel("X position")
        plt.title("X position Vs Time")

        a = np.polyfit(nsteptruncated, xtruncated, 1)
        print(f"The velocity of the {set} is {a[0].round(2)}")

        fig2 = plt.figure("Figure 2")
        plt.plot(nstepslist, ylist)
        plt.xlabel("Time step")
        plt.ylabel("Y position")
        plt.title("Y position Vs Time")

        plt.show()

    elif set == "toad":
        grid.toad()

    elif set == "lightship":
        grid.lightship()
        alivelist = []
        nstepslist = np.arange(0, nsteps, 1)
        for n in range(nsteps):
            grid.conways_game()
            alivelist.append(grid.summing())
            # show animation
            plt.cla()
            im = plt.imshow(grid.grid_array, animated=True, vmin=0, vmax=1)
            plt.draw()
            plt.pause(0.0001)
            if n % 10 == 0:
                print(n)

        fig2 = plt.figure("Figure 2")
        plt.plot(nstepslist, alivelist)
        plt.show()
    else:
        print("NOT A VALID SET")
