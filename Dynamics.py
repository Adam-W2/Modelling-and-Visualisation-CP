import matplotlib
matplotlib.use("TKAgg")
import numpy as np
import random
import matplotlib.animation as animation
import matplotlib.pyplot as plt

def Kawasaki(X,Y,kT,spins):
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
                distance = np.sqrt(min([diffx,X - diffx]) ** 2 + min([diffy,Y - diffy]) ** 2)
                if distance == 1:
                    Edelta -= 1

                r = random.random()
                if r <= np.exp(-Edelta / kT):
                    spins[itrial1,jtrial1] = spin1
                    spins[itrial2,jtrial2] = spin2


def Glauber(X,Y,kT,spins):
    for i in range(X):
        for j in range(Y):
            itrial = np.random.randint(0,X)
            jtrial = np.random.randint(0,Y)
            spin_new = -spins[itrial,jtrial]

            Edelta = -2 * spin_new * (spins[(itrial + 1) % X][jtrial] + spins[(itrial - 1) % X][jtrial] +
                                      spins[itrial][(jtrial + 1) % X] + spins[itrial][(jtrial - 1) % X])

            r = random.random()
            if r <= np.exp(-Edelta / kT):
                spins[itrial,jtrial] = spin_new


def measure(X,Y,spins):
    E = 0
    M = 0
    E2 = 0
    modM = 0
    M2 = 0
    for i in range(X):
        for j in range(Y):
            E += -1/2 * spins[i][j] * (spins[(i + 1) % X][j] + spins[(i - 1) % X][j] + spins[i][(j + 1) % X] +
                                     spins[i][(j - 1) % X])
            M += spins[i][j]

    return E,M


def calc_ob(X,kT,E,M,E2,M2):
    c = (E2-np.power(E,2))/(np.power(X,2) * np.power(kT,2))
    x = (M2-np.power(M,2))/(np.power(X,2) * kT)
    return c,x


def run_dynamics(nsteps,X,D,kT,spins):
    Y = X

    if D == "G":
        Elist = []
        Mlist = []
        E2list = []
        modMlist = []
        M2list = []
        for n in range(nsteps):
            Glauber(X,Y,kT,spins)
            if n % 10 == 0:
                E,M = measure(X,Y,spins)
                Elist.append(E)
                E2list.append(E**2)
                Mlist.append(M)
                modMlist.append(np.absolute(M))
                M2list.append(M**2)

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

        avE = sum(Elist)/len(Elist)
        avE2 = sum(E2list)/len(E2list)
        avM = sum(Mlist)/len(Mlist)
        avmodM = sum(modMlist)/len(modMlist)
        avM2 = sum(M2list)/len(M2list)
        c,x = calc_ob(X,kT,avE,avM,avE2,avM2)

        return avE,avM,avmodM,c,x



    elif D == "K":
        Elist = []
        Mlist = []
        E2list = []
        modMlist = []
        M2list = []
        for n in range(nsteps):
            Kawasaki(X,Y,kT,spins)
            if n % 10 == 0 and n > 100:
                E,M = measure(X,Y,spins)
                Elist.append(E)
                E2list.append(E**2)
                Mlist.append(M)
                modMlist.append(np.absolute(M))
                M2list.append(M**2)
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

        avE = sum(Elist) / len(Elist)
        avE2 = sum(E2list) / len(E2list)
        avM = sum(Mlist) / len(Mlist)
        avmodM = sum(modMlist) / len(modMlist)
        avM2 = sum(M2list) / len(M2list)
        c,x = calc_ob(X,kT,avE,avM,avE2,avM2)

        return avE,avM,avmodM,c,x
    else:
        print("Incorrect dynamics given, check your spelling?")


