import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from Grid import Grid

N = 51
error = 1e-3
grid = Grid(N)

#TO DO#
#Need to use pandas dataframe instead of numpy array txt
#Update plots with colour bar and create plots of final files
#Allow for user input as well

which = "jac"
if which == "jac":
    grid.initialrho()

    flag = True
    while flag:
        old,new = grid.steps()
        if abs(old - new) < error:
            flag = False

    x,y,z = grid.efield()

    dfpot = pd.DataFrame(grid.grid[25,:,:])
    dfx = pd.DataFrame(x)
    dfy = pd.DataFrame(y)
    dfz = pd.DataFrame(z)
    dfpot.to_csv("Data/Potential_final.csv")
    dfx.to_csv("Data/Ex_final.csv")
    dfy.to_csv("Data/Ey_final.csv")
    dfz.to_csv("Data/Ez_final.csv")

elif which == "gauss":
    grid.initialrho()

    flag = True
    while flag:
        old, new = grid.step_gauss()
        if abs(old - new) < error:
            flag = False

    x, y, z = grid.efield()
    dfpot = pd.DataFrame(grid.grid[25,:,:])
    dfx = pd.DataFrame(x)
    dfy = pd.DataFrame(y)
    dfz = pd.DataFrame(z)
    dfpot.to_csv("Data/Potential_gauss_final.csv")
    dfx.to_csv("Data/Ex_gauss_final.csv")
    dfy.to_csv("Data/Ey_gauss_final.csv")
    dfz.to_csv("Data/Ez_gauss_final.csv")

elif which == "mag":
    grid.initialrho_wire()

    flag = True
    while flag:
        old,new = grid.step_mag()
        if abs(old-new) < error:
            flag = False
    Bx, By = grid.bfield()
    dfpot = pd.DataFrame(grid.grid[25,:,:])
    dfx = pd.DataFrame(Bx).round(8)
    dfy = pd.DataFrame(By)
    dfpot.to_csv("Data/Potential_mag_final.csv")
    dfx.to_csv("Data/Bx_final.csv")
    dfy.to_csv("Data/By_final.csv")

else:
    grid.initialrho()
    wlist = np.linspace(1.5,2,50)
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