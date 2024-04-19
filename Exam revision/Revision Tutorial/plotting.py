import matplotlib
matplotlib.use("TKAgg")
import matplotlib.pyplot as plt
from Grid import Grid
import pandas as pd
import numpy as np

grid = pd.read_csv("grid.csv",header=None,index_col = False)
grid = grid.drop(0,axis= 0).drop(0,axis=1)
print(grid.head())
grid = np.array(grid)

center_point = np.array((int(grid.shape[0] / 2.), int(grid.shape[1] / 2.)))
points = np.argwhere(grid <= 1000)
rsquare = ((points - center_point)**2).sum(axis=1).reshape((50,50))

gridlist = np.ravel(grid)
rlist = np.ravel(np.sqrt(rsquare))

indices = np.argsort(rlist)

gridlist = gridlist[indices]
rlist = rlist[indices]

plt.plot(rlist,gridlist)
plt.show()