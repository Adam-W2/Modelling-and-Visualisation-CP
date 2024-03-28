import matplotlib.pyplot as plt
import numpy as np

from Grid import Grid

N = 51
error = 1e-3
grid = Grid(N)

which = "j"
if which == "jac":
    grid.initialrho()

    flag = True
    while flag:
        old,new = grid.steps()
        if abs(old - new) < error:
            flag = False

    x,y,z = grid.efield()
    np.savetxt("Ex1.csv",x,delimiter=",")
    np.savetxt("Ey1.csv",y,delimiter=",")
    np.savetxt("Ez1.csv",z,delimiter=",")
    np.savetxt("Potential1.csv",grid.grid[50,:,:],delimiter=",")
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
    Bx, By = grid.bfield()
    np.savetxt("Mx1.csv", Bx, delimiter=",")
    np.savetxt("My1.csv", By, delimiter=",")

    np.savetxt("Potential_mag.csv", grid.grid[25, :, :], delimiter=",")