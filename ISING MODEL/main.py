import matplotlib
matplotlib.use("TKAgg")
import numpy as np
import random
from Dynamics import run_dynamics
import pandas as pd
from Animation import animations

"""""
This main file initilises the arrays and runs the dynamics for a range of temperatures
Choose between running the animation by entering Y for the animation option the follow instructions.
For measurements enter N then input desired values.
"""""

ani = input("Animation: ")

if ani == "Y":
    N, nsteps, D, T = input("Input size of array, sweeps, type of dynamic and temperature: ").split(" ")

    X = int(N)
    Y = X
    kT = float(T)
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
    N, nsteps, D = input("Input size of array, sweeps and type of dynamic: ").split(" ")
    X = int(N)
    Y = X
    nsteps = int(nsteps)

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
    df.insert(0,"Temperature",T)
    df.to_csv("Data/Simulation_Data_Glauber",index = False)