import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from numpy import genfromtxt

fig1 = plt.figure("Figure 1")
file = "Data/WithError1.csv"
df = pd.read_csv(file)
p1list = np.arange(0.2,0.5,0.02)
plt.errorbar(p1list,df["Counts"],yerr=df["error"],capsize=2, markeredgewidth=1)
plt.xlabel("probability 1")
plt.ylabel("Varaiance")

fig2 = plt.figure("Figure 2")
p3list = np.arange(0,1,0.05)
my_data = genfromtxt('Data/array2.csv',delimiter=',')
my_data = np.flipud(my_data)
plt.imshow(my_data,extent = [0,1,0,1])
plt.title("Matrix of p1 vs p3 with constant p2")

fig3 = plt.figure("Figure 3")
file = "Data/Immune1.csv"
df = pd.read_csv(file)
plt.plot(df["Immune Fraction"],df["Infected Fraction"])
plt.xlabel("Immune Fraction")
plt.ylabel("Infected Fraction")
plt.show()