import matplotlib
matplotlib.use("TKAgg")
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("Data/test2_100000.csv")

plt.plot(df["step"],df["Free energy"])
plt.xlabel("Step")
plt.ylabel("Free Energy")
plt.show()