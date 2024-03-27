import matplotlib.pyplot as plt
import numpy as np

from Grid import Grid

N = 51
error = 1e-3
grid = Grid(N)

which = "pee"
if which == "jac":
    grid.initialrho()

    flag = True
    while flag:
        old,new = grid.steps()
        if abs(old - new) < error:
            flag = False

    x,y,z = grid.efield()
    np.savetxt("Ex.csv",x,delimiter=",")
    np.savetxt("Ey.csv",y,delimiter=",")
    np.savetxt("Ez.csv",z,delimiter=",")
    np.savetxt("Potential.csv",grid.grid[50,:,:],delimiter=",")
elif which == "gauss":
    grid.initialrho()

    flag = True
    while flag:
        old, new = grid.step_gauss()
        if abs(old - new) < error:
            flag = False

    x, y, z = grid.efield()
    np.savetxt("Ex_gauss.csv", x, delimiter=",")
    np.savetxt("Ey_gauss.csv", y, delimiter=",")
    np.savetxt("Ez_gauss.csv", z, delimiter=",")
    np.savetxt("Potential_gauss.csv", grid.grid[25, :, :], delimiter=",")
else:
    grid.initialrho_wire()
    flag = True
    while flag:
        old,new = grid.steps()
        if abs(old-new) < error:
            flag = False
    x, y, z = grid.efield()
    np.savetxt("Mx.csv", x, delimiter=",")
    np.savetxt("My.csv", y, delimiter=",")
    np.savetxt("Mz.csv", z, delimiter=",")
    np.savetxt("Potential_mag.csv", grid.grid[25, :, :], delimiter=",")