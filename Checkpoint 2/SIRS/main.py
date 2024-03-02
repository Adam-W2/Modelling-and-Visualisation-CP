from Grid import Grid
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#wave state: p1 = 0.8, p2 = 0.3, p3 = 0.01
#N,nstep,p1,p2,p3 = input("Please input N,nsteps,p1,p2 and p3: ").split()
N = 50
nstep = 10000
p1 = 0.8
p2 = 0.1
p3 = 0.01

nsteps = int(nstep)
grid = Grid(int(N), float(p1), float(p2), float(p3))

which = "animatio"
if which == "animation":
    grid.create_random_grid()
    grid.animation(nsteps)

else:
    measure = "bot"
    if measure == "both":
        p3list = np.arange(0,1,0.05)
        p1list = np.arange(0,1,0.05)
        size = len(p3list)
        p2 = 0.5
        n = 0
        x = 0
        y = 0
        matrix = np.zeros((size,size))
        for p1 in p1list:
            y = 0
            for p3 in p3list:

                grid = Grid(int(N), float(p1), float(p2), float(p3))
                grid.create_random_grid()

                average = grid.measure_contour(nsteps)
                matrix[x,y] = average/(N**2)
                n += 1
                print(f"{100 * n/len(p1list)**2}% calculated...")
                y += 1
            x += 1

        plt.imshow(matrix)
        plt.show()
        #np.savetxt("array1.csv",matrix,delimiter=",")
    else:
        p1list = np.arange(0.2,0.5,0.02)
        nsteps = 10000
        p3 = 0.5
        p2 = 0.5
        n = 0
        averages = []
        errors = []

        for p1 in p1list:

            grid = Grid(int(N),float(p1),float(p2),float(p3))
            grid.create_random_grid()

            average,error = grid.measure_contour(nsteps)
            averages.append(average)
            errors.append(error)

            n += 1
            print(f"{100 * n / len(p1list)}% calculated...")

        df = pd.DataFrame({"Counts":averages,"error":errors})
        df.to_csv("WithError1.csv",index= False)
        plt.errorbar(p1list,df["Counts"],yerr=df["error"],capsize=2, markeredgewidth=1)
        plt.show()