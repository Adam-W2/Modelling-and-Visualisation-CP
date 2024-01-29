import matplotlib
matplotlib.use("TKAgg")
import numpy as np
import random
import matplotlib.animation as animation
import matplotlib.pyplot as plt

nsteps = 10000
N, T, D = input("Input size of array, temperature and type of dynamics: ").split(" ")
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
if D == "Glauber":
    for n in range(nsteps):
        for i in range(X):
            for j in range(Y):
                itrial = np.random.randint(0,X)
                jtrial = np.random.randint(0,Y)
                spin_new = -spins[itrial,jtrial]

                Edelta = -2 * spin_new * (spins[(itrial + 1) % X][jtrial] + spins[(itrial - 1) % X][jtrial] +
                                          spins[itrial][(jtrial + 1) % X] + spins[itrial][(jtrial - 1) % X])

                r = random.random()
                if r <= np.exp(-Edelta/kT):
                    spins[itrial,jtrial] = spin_new

        if n % 5 == 0:
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
            im = plt.imshow(spins, animated=True,vmin =-1,vmax=1)
            plt.draw()
            plt.pause(0.00001)

elif D == "Kawasaki":
    for n in range(nsteps):
        for i in range(X):
            for j in range(Y):
                itrial1 = np.random.randint(0,X)
                jtrial1 = np.random.randint(0,Y)
                itrial2 = np.random.randint(0,X)
                jtrial2 = np.random.randint(0,Y)

                spin1 = spins[itrial1][jtrial1]
                spin2 = spins[itrial2][jtrial2]

                if spin1 != spin2:
                    spin1 = -1 * spin1
                    spin2 = -1 * spin2
                    diffx = itrial1 - itrial2
                    diffy = jtrial1 - jtrial2

                    Edelta1 = -2 * spin1 * (spins[(itrial1 + 1) % X][jtrial1] + spins[(itrial1 - 1) % X][jtrial1] +
                                              spins[itrial1][(jtrial1 + 1) % X] + spins[itrial1][(jtrial1 - 1) % X])

                    Edelta2 = -2 * spin2 * (spins[(itrial2 + 1) % X][jtrial2] + spins[(itrial2 - 1) % X][jtrial2] +
                                              spins[itrial2][(jtrial2 + 1) % X] + spins[itrial2][(jtrial2 - 1) % X])

                    Edelta = Edelta1 + Edelta2
                    distance = np.sqrt(min([diffx,X - diffx])**2 + min([diffy, Y - diffy])**2)
                    if distance == 1:
                        Edelta -= 1

                    r = random.random()
                    if r <= np.exp(-Edelta / kT):
                        spins[itrial1, jtrial1] = spin1
                        spins[itrial2, jtrial2] = spin2
        if n % 5 == 0:
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
            im = plt.imshow(spins, animated=True,vmin =-1,vmax=1)
            plt.draw()
            plt.pause(0.00001)
else:
    print("Incorrect dynamics given, check your spelling?")

#start temp 1, for glauber all up or down, start random is okay but get stripe. The you have to wait to get rid of sttripe. Start all up or down to calculate temp