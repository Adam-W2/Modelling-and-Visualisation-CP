import pandas as pd
import matplotlib.pyplot as plt
file = "test2.csv"
sr = pd.read_csv(file)
print(sr.head())
plt.hist(sr["nsteps"],50)
plt.show()