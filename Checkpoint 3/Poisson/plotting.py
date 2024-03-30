import matplotlib
matplotlib.use("TKAgg")
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

Potential = pd.read_csv("Data/Potential_mag_final.csv",header=None,index_col = False)
Potential = Potential.drop(0,axis= 0).drop(0,axis=1)
xgrad = pd.read_csv("Data/Bx_final.csv",header=None,index_col = False)
xgrad = xgrad.drop(0,axis= 0).drop(0,axis=1)
ygrad = pd.read_csv("Data/By_final.csv",header=None,index_col = False)
ygrad = ygrad.drop(0,axis= 0).drop(0,axis=1)
zgrad = pd.read_csv("Data/Ez_gauss_final.csv",header=None,index_col = False)
zgrad = zgrad.drop(0,axis= 0).drop(0,axis=1)

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
    plt.savefig("Plots/Potential_mag")
    plt.show()
fig3 = plt.figure("Figure 3")
plt.quiver(xnorm,ynorm)
plt.title("Normalised")
plt.savefig("Plots/Bfield_norm")

fig4 = plt.figure("Figure 4")
plt.quiver(xgrad,ygrad)
plt.title("Bfield")
plt.savefig("Plots/Bfield")
plt.show()