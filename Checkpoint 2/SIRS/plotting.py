import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from numpy import genfromtxt

fig1 = plt.figure("Figure 1")
file = "WithError1.csv"
df = pd.read_csv(file)
p1list = np.arange(0.2,0.5,0.02)
plt.errorbar(p1list,df["Counts"],yerr=df["error"],capsize=2, markeredgewidth=1)


fig2 = plt.figure("Figure 2")
p3list = np.arange(0,1,0.05)
my_data = genfromtxt('array2.csv', delimiter=',')
my_data = np.flipud(my_data)
plt.imshow(my_data,extent = [0,1,0,1])

fig3 = plt.figure("Figure 3")
file = "Immune1.csv"
df = pd.read_csv(file)
plt.plot(df["Immune Fraction"],df["Infected Fraction"])

plt.show()