import matplotlib
matplotlib.use("TKAgg")
import numpy as np
import random
import matplotlib.animation as animation
import matplotlib.pyplot as plt


nsteps = 10000
N, T = input("Input size of array and temperature: ").split(" ")
X = int(N)
Y = X
kT = float(T)
spins = np.zeros((X,Y))

for i in range(X):
    for j in range(Y):
        r = random.random()
        if r < 0.5: spins[i,j] = -1
        else: spins[i,j] = 1

fig = plt.figure()
im = plt.imshow(spins, animated=True)

for n in range(nsteps):
    for i in range(X):
        for j in range(Y):
            itrial = np.random.randint(0,X)
            jtrial = np.random.randint(0,Y)
            spin_new = -spins[itrial,jtrial]

            left = (itrial - 1) + 1
            right = (itrial + 1) + 1
            top = (jtrial - 1) + 1
            bot = (jtrial + 1) + 1

            #ghost_array = np.pad(spins,(1,1),"wrap")
            Edelta = -2 * spin_new * (spins[(itrial + 1) % X][jtrial] + spins[(itrial - 1) % X][jtrial] +
                                 spins[itrial][(jtrial + 1) % X] + spins[itrial][(jtrial - 1) % X])

            r = random.random()
            if r <= np.exp(-Edelta/kT):
                spins[itrial,jtrial] = spin_new

    if n % 10 == 0:
        #update measurements
        #dump output (e.g., for gnuplot)
        """""
        f = open('spins.dat', 'w')
        for i in range(X):
            for j in range(Y):
                f.write('%d %d %lf\n' % (i, j, spins[i, j]))
        f.close()
        """""
        #show animation
        plt.cla()
        im = plt.imshow(spins, animated=True)
        plt.draw()
        plt.pause(0.0001)








