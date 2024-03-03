from Grid import Grid
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#absorbing: p1 = 0.5, p2 = 0.6, p3 = 0.1
#dynamic: p1 = 0.5, p2 = 0.6, p3 = 0.45
#wave state: p1 = 0.8, p2 = 0.1, p3 = 0.01
#N,nstep,p1,p2,p3 = input("Please input N,nsteps,p1,p2 and p3: ").split()
N = 50
nstep = 1000
p1 = 0.8
p2 = 0.1
p3 = 0.01
nsteps = int(nstep)

which = "animatio"
if which == "animation":
    """""
    This part of the code runs just the animation for selected probabilites
    """""
    nsteps = int(nstep)
    grid = Grid(int(N),float(p1),float(p2),float(p3))
    grid.create_random_grid()
    grid.animation(nsteps)

else:
    """""
    This part of the code calculates the contour plot with varying p1 and p3
    """""
    measure = "set"
    if measure == "both":
        p3list = np.arange(0,1,0.05)
        p1list = np.arange(0,1,0.05)
        size = len(p3list)
        p2 = 0.5
        n = 0
        x = 0
        y = 0
        matrix = np.zeros((size,size))
        for p3 in p1list:
            y = 0
            for p1 in p3list:

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
        np.savetxt("array2.csv",matrix,delimiter=",")
    elif measure == "set":
        """""
        This part of the code is for plotting the set p3 value variance plot with error bars
        REMEMBER TO ADD THE ERROR CALC BACK IN!!!!
        """""
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

            I,I2,error = grid.measure_contour(nsteps)
            averages.append((I2-I**2)/N**2)
            errors.append(error)

            n += 1
            print(f"{100 * n / len(p1list)}% calculated...")

        df = pd.DataFrame({"Counts":averages,"error":errors})
        df.to_csv("WithError1.csv",index= False)
        plt.errorbar(p1list,df["Counts"],yerr=df["error"],capsize=2, markeredgewidth=1)
        plt.show()
    else:
        """""
        This part of the code calculates the immunity fraction effect
        """""
        p1 = 0.5
        p2 = 0.5
        p3 = 0.5
        immunelist = np.arange(0,1,0.05)
        average = []
        n = 0

        for i in immunelist:
            temp = []
            for _ in range(5):

                grid = Grid(int(N),float(p1),float(p2),float(p3))
                grid.create_random_grid()
                grid.add_immune_cells(i)
                I = grid.measure_contour(nsteps)
                temp.append(I)
            avgtemp = sum(temp)/len(temp)
            average.append(avgtemp/N**2)
            n += 1
            print(f"{100 * n / len(immunelist)}% calculated...")

        df = pd.DataFrame({"Infected Fraction":average,"Immune Fraction":immunelist})
        df.to_csv("Immune1.csv",index= False)
        plt.plot(immunelist,df["Counts"])
        plt.show()