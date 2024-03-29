import matplotlib
matplotlib.use("TKAgg")
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

Potential = pd.read_csv("Data/Potential_final.csv")
xgrad = pd.read_csv("Data/Ex_final.csv")
ygrad = pd.read_csv("Data/Ey_final.csv")
zgrad = pd.read_csv("Data/Ez_final.csv")

xgrad = np.array(xgrad)
ygrad = np.array(ygrad)
zgrad = np.array(zgrad)

xnorm = xgrad/np.sqrt(xgrad**2+ygrad**2+zgrad**2)
ynorm = ygrad/np.sqrt(xgrad**2+ygrad**2+zgrad**2)
znorm = zgrad/np.sqrt(xgrad**2+ygrad**2+zgrad**2)

Potential = np.array(Potential)
when = "now"

if when == "now":
    fig2 = plt.figure("Figure 2")
    plt.imshow(Potential)
    plt.colorbar()
    plt.title("Potential")

    plt.show()
fig3 = plt.figure("Figure 3")
plt.quiver(xnorm,ynorm)
plt.title("Normalised")

fig4 = plt.figure("Figure 4")
print(xgrad.shape)
print(ygrad.shape)
plt.quiver(xgrad,ygrad)
plt.show()