import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from Grid import Grid

N = 51
error = 1e-3
grid = Grid(N)

which = "mag"
if which == "jac":
    grid.initialrho()

    flag = True
    while flag:
        old,new = grid.steps()
        if abs(old - new) < error:
            flag = False

    x,y,z = grid.efield()
    np.savetxt("Data/Ex_final.csv",x,delimiter=",")
    np.savetxt("Data/Ey_final.csv",y,delimiter=",")
    np.savetxt("Data/Ez_final.csv",z,delimiter=",")
    np.savetxt("Data/Potential_final.csv",grid.grid[25,:,:],delimiter=",")
elif which == "gauss":
    grid.initialrho()

    flag = True
    while flag:
        old, new = grid.step_gauss()
        if abs(old - new) < error:
            flag = False

    x, y, z = grid.efield()
    np.savetxt("Data/Ex_gauss_final.csv", x, delimiter=",")
    np.savetxt("Data/Ey_gauss_final.csv", y, delimiter=",")
    np.savetxt("Data/Ez_gauss_final.csv", z, delimiter=",")
    np.savetxt("Data/Potential_gauss_final.csv", grid.grid[25, :, :], delimiter=",")
elif which == "mag":
    grid.initialrho_wire()
    flag = True
    while flag:
        old,new = grid.step_mag()
        if abs(old-new) < error:
            flag = False
    Bx, By = grid.bfield()
    print(Bx.shape)
    print(By.shape)
    np.savetxt("Data/Mx_final.csv", Bx, delimiter=",")
    np.savetxt("Data/My_final.csv", By, delimiter=",")
    plt.imshow(grid.grid[25,:,:])
    plt.show()
    np.savetxt("Data/Potential_mag_final.csv", grid.grid[25, :, :], delimiter=",")

else:
    grid.initialrho()
    wlist = np.linspace(1.5,2,25)
    nlist = []
    for i in wlist:
        n = 0
        flag = True
        grid.reset()
        while flag:
            old,new = grid.overrelax(i)
            n += 1
            if n % 100 == 0:
                print(n)
            if abs(old - new) < error:
                flag = False
        nlist.append(n)
        print(f"Completed w = {i}")

    df = pd.DataFrame({"w":wlist,"step count":nlist})
    df.to_csv("Data/overrelax_datafile.csv",index=False)
    x,y,z = grid.efield()
    np.savetxt("Data/Ex_over.csv",x,delimiter=",")
    np.savetxt("Data/Ey_over.csv",y,delimiter=",")
    np.savetxt("Data/Ez_over.csv",z,delimiter=",")
    np.savetxt("Data/Potential2.csv",grid.grid[50,:,:],delimiter=",")
