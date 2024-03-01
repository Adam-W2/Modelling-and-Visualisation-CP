from Grid import Grid
import numpy as np
import matplotlib.pyplot as plt

#wave state: p1 = 0.8, p2 = 0.3, p3 = 0.01
#N,nstep,p1,p2,p3 = input("Please input N,nsteps,p1,p2 and p3: ").split()
N = 50
nstep = 500
p1 = 0.8
p2 = 0.1
p3 = 0.01

nsteps = int(nstep)
grid = Grid(int(N), float(p1), float(p2), float(p3))

which = "a"
if which == "animation":
    grid.create_random_grid()
    grid.animation(nsteps)

else:
    p3list = np.arange(0,1,0.02)
    p1list = np.arange(0,1,0.02)
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
            print(f"{n/len(p1list)**2}% calculated...")
            y += 1
        x += 1

    plt.imshow(matrix)
    plt.show()
    np.savetxt("array1.csv",matrix,delimiter=",")