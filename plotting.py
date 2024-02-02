import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

name = "Simulation_Data_Glauber"

df = pd.read_csv(name)
T = np.linspace(1,3,20)

col = list(df.columns)

col = [x for x in col if "Error" or "Temperature" not in x]
col_error = [x for x in col if "Error" in x]
"""""
for i in col:
    if i == "Specific Heat":
        plt.errorbar(T,df[i],yerr=df["Error c boot"],capsize=20, elinewidth=3, markeredgewidth=10)
        plt.errorbar(T,df[i],yerr=df["Error c jack"],capsize=20,elinewidth=3,markeredgewidth=10)

    elif i == "Susepctibility":
        plt.errorbar(T,df[i],yerr=df["Error c boot"],capsize=20, elinewidth=3, markeredgewidth=10)
        plt.errorbar(T,df[i],yerr=df["Error c jack"],capsize=20,elinewidth=3,markeredgewidth=10)
    else:
        plt.figure()
        plt.plot(T,df[i])
        plt.xlabel("Temperature (K)")
        plt.ylabel(i)
"""""
fig1 = plt.figure("Figure 1")
plt.errorbar(T,df["Specific Heat"],yerr=df["Error c boot"],capsize=2, markeredgewidth=1)
plt.title("Bootstrap")
fig2 = plt.figure("Figure 2")
plt.errorbar(T,df["Specific Heat"],yerr=df["Error x boot"],capsize=2, markeredgewidth=1)
plt.title("Jacknife")
#plt.plot(T,df["Specific Heat"])
plt.show()
#Error c jack = Error x boot