import pandas as pd
import matplotlib.pyplot as plt
file = "Data/test2.csv"
sr = pd.read_csv(file)
print(sr.head())
plt.hist(sr["nsteps"],50)
plt.xlabel("Nsteps")
plt.ylabel("Counts")
plt.title("Number of simulations versus nsteps")
plt.show()