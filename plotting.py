import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("Simulation_Data_Kawasaki")

T = np.linspace(1,3,20)
col = list(df.columns)

col = [x for x in col if "Error" not in x]
col_error = [x for x in col if "Error" in x]

for i in col:
    plt.figure()
    plt.plot(T,df[i])
    plt.xlabel("Temperature (K)")
    plt.ylabel(i)
plt.show()