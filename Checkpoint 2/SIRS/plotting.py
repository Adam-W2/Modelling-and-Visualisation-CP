import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from numpy import genfromtxt

file = "WithError1.csv"
df = pd.read_csv(file)
p1list = np.arange(0.2,0.5,0.02)
plt.errorbar(p1list,df["Counts"],yerr=df["error"],capsize=2, markeredgewidth=1)
plt.show()

p3list = np.arange(0,1,0.05)
my_data = genfromtxt('array2.csv', delimiter=',')
my_data = np.flipud(my_data)
plt.imshow(my_data,extent = [0,1,0,1])
plt.show()