import matplotlib
matplotlib.use("TKAgg")
import numpy as np
import random
from Dynamics import run_dynamics
import pandas as pd
from Animation import animations

"""""
This main file initilises the arrays and runs the dynamics for a range of temperatures
Choose between running the animation by entering Y for the animation option.
For measurements enter N
"""""

ani = input("Animation: ")

if ani == "Y":
    N, nsteps, D, T = input("Input size of array, sweeps, type of dynamic and temperature: ").split(" ")

    X = int(N)
    Y = X
    kT = int(T)
    nsteps = int(nsteps)
    spins = np.ones((X,Y))

    for i in range(X):
        for j in range(Y):
            r = random.random()
            if r < 0.5:
                spins[i, j] = -1
            else:
                spins[i, j] = 1

    animations(nsteps,X,D,kT,spins)

else:
    N, D, nsteps = input("Input size of array, sweeps and type of dynamic: ").split(" ")
    X = int(N)
    Y = X

    if D == "G":
        spins = np.ones((X,Y))
        cols = ["Energy", "Magnetism", "modulus Magnetism", "Specific Heat", "Susepctibility", "Error c boot",
                "Error c jack", "Error x boot", "Error x jack"]
        dic1 = [[], [], [], [], [], [], [], [], []]
    else:
        spins = np.ones((X,Y))
        spins[:int(X/2),:] = -1
        cols = ["Energy", "Specific Heat", "Error c boot",
                "Error c jack"]
        dic1 = [[], [], [], []]

    T = np.linspace(1,3,20)
    for i in T:
        L,spin = run_dynamics(nsteps,X,D,i,spins)
        spins = spin
        for j in range(len(L)):
            dic1[j].append(L[j])
        print(i)
    dic = {}
    for i in range(len(dic1)):
        dic.update({cols[i]:dic1[i]})

    df = pd.DataFrame(dic)
    df.to_csv("Simulation_Data_Kawasaki")