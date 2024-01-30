import matplotlib
matplotlib.use("TKAgg")
import numpy as np
import random
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from Dynamics import run_dynamics
import pandas as pd

nsteps = 10000
N, T, D = input("Input size of array, temperature and type of dynamics: ").split(" ")
X = int(N)
Y = X
kT = float(T)
spins = np.ones((X,Y))
"""""
for i in range(X):
    for j in range(Y):
        r = random.random()
        if r < 0.5: spins[i,j] = -1
        else: spins[i,j] = 1
"""""
fig = plt.figure()
im = plt.imshow(spins, animated=True)
T = np.linspace(1,3,20)
print(T)
Elist = []
Mlist = []
modMlist = []
clist = []
xlist = []

for i in T:
    E,M,modM,c,x = run_dynamics(nsteps,X,D,i,spins)
    print(E,M,modM,c,x)
    Elist.append(E)
    Mlist.append(M)
    modMlist.append(np.absolute(modM))
    clist.append(c)
    xlist.append(x)

df = pd.DataFrame({"Energy":Elist,"Magnetism":Mlist,"modulus Magnetism":modMlist,"Specific Heat":clist,"Susepctibility":xlist})
df.to_csv("Simulation_Data")



#start temp 1, for glauber all up or down, start random is okay but get stripe. The you have to wait to get rid of sttripe. Start all up or down to calculate temp
