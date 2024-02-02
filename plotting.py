import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("Simulation_Data_Kawasaki")
df.drop("Unnamed: 0", axis = 1, inplace= True)
print(df.head())
T = np.linspace(1,3,20)
col = list(df.columns)

for i in col:
    plt.figure()
    plt.plot(T,df[i])
    plt.xlabel("Temperature (K)")
    plt.ylabel(i)
plt.show()