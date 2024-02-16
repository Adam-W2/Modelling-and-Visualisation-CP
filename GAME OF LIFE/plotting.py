import pandas as pd
import matplotlib.pyplot as plt
file = "test1.csv"
sr = pd.read_csv(file)

plt.hist(sr)