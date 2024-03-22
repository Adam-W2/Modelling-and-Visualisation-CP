import matplotlib
matplotlib.use("TKAgg")
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

Efield = pd.read_csv("Efield.csv")
Potential = pd.read_csv("Potential.csv")
xgrad = pd.read_csv("xgrad.csv")
ygrad = pd.read_csv("ygrad.csv")
zgrad = pd.read_csv("zgrad.csv")

xgrad = np.array(xgrad)
ygrad = np.array(ygrad)
zgrad = np.array(zgrad)
Efield = np.array(Efield)
Potential = np.array(Potential)
when = "no"

if when == "now":
    fig1 = plt.figure("Figure 1")
    plt.imshow(Efield)
    plt.title("E-Field")

    fig2 = plt.figure("Figure 2")
    plt.imshow(Potential)
    plt.title("Potential")

    plt.show()
print(ygrad)
plt.quiver(xgrad,ygrad)
plt.show()