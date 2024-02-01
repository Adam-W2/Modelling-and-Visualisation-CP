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

cols = ["Energy","Magnetism","modulus Magnetism","Specific Heat","Susepctibility","Error c boot","Error c jack","Error x boot", "Error x jack"]
dic1 = [[],[],[],[],[],[],[],[],[]]

for i in T:
    L = run_dynamics(nsteps,X,D,i,spins)
    for j in range(len(L)):
        dic1[j].append(L[j])
    print(i)
dic = {}
for i in range(len(dic1)):
    dic.update({cols[i]:dic1[i]})

df = pd.DataFrame(dic)
df.to_csv("Simulation_Data_Glauber")


#start temp 1, for glauber all up or down, start random is okay but get stripe. The you have to wait to get rid of sttripe. Start all up or down to calculate temp
