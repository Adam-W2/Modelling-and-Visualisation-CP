import matplotlib
matplotlib.use("TKAgg")
import matplotlib.pyplot as plt
from Grid import Grid
import numpy as np
import pandas as pd
df = pd.read_csv("Data/test2_100000.csv")

plt.plot(df["step"],df["Free energy"])
plt.xlabel("Step")
plt.ylabel("Free Energy")
plt.show()