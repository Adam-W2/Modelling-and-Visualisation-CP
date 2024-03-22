import matplotlib.pyplot as plt
import numpy as np

from Grid import Grid

N = 51
error = 1e-3
grid = Grid(N)

grid.initialrho()

flag = True
while flag:
    old,new = grid.steps()
    if abs(old - new) < error:
        flag = False

E,x,y,z = grid.efield()
#fig1 = plt.figure("Figure 1")
#plt.imshow(grid.grid[50,:,:])
#plt.colorbar()

#fig2 = plt.figure("Figure 2")
#plt.imshow(E[:,:,50])
#plt.quiver([],E[:,50,:],E[:,:,5])

#plt.colorbar()

plt.show()
np.savetxt("xgrad.csv",x,delimiter=",")
np.savetxt("ygrad.csv",y,delimiter=",")
np.savetxt("zgrad.csv",z,delimiter=",")
np.savetxt("Efield.csv",E[:,:,50],delimiter=",")
np.savetxt("Potential.csv",grid.grid[50,:,:],delimiter=",")