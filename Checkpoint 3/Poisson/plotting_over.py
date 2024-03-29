import matplotlib
matplotlib.use("TKAgg")
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("Data/overrelax_datafile.csv")

plt.plot(df["w"],df["step count"])
plt.xlabel("w")
plt.ylabel("step count")
plt.title("value of w versus step count")
plt.show()