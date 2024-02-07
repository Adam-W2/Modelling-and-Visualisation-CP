import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

name = "Simulation_Data_Glauber_main"

df = pd.read_csv(name)
T = np.linspace(1,3,20)

fig1 = plt.figure("Figure 1")
plt.errorbar(T,df["Specific Heat"],yerr=df["Error c boot"],capsize=2, markeredgewidth=1)
plt.title("Specific Heat with bootstrap error calculation")
plt.xlabel("Temperature (K)")
plt.ylabel("Specific Heat")

fig2 = plt.figure("Figure 2")
plt.errorbar(T,df["Specific Heat"],yerr=df["Error c jack"],capsize=2, markeredgewidth=1)
plt.title("Specific Heat with jacknife error calculation")
plt.xlabel("Temperature (K)")
plt.ylabel("Specific Heat")

fig3 = plt.figure("Figure 3")
plt.plot(T,df["Energy"])
plt.title("Energy")
plt.xlabel("Temperature (K)")
plt.ylabel("Energy")

plt.show()

print(df["Specific Heat"].max())
#Error c jack = Error x boot