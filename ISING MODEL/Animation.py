import matplotlib
matplotlib.use("TKAgg")
import matplotlib.pyplot as plt
from Dynamics import Glauber,Kawasaki


def animations(nsteps, X, D, kT, spins):
    """""
    Function that runs the animation aspect without any measurement taking
    This has been done so it can be ran seperately to the measurement taking.
    """""

    Y = X
    if D == "G":
        # Loop over number of desired sweeps updating the spins each sweep
        for n in range(nsteps):

            Glauber(X, Y, kT, spins)
            if n % 10 == 0:

                # show animation
                plt.cla()
                im = plt.imshow(spins, animated=True, vmin=-1, vmax=1)
                plt.draw()
                plt.pause(0.00001)

        return spins

    elif D == "K":

        for n in range(nsteps):
            Kawasaki(X, Y, kT, spins)
            if n % 10 == 0:

                # show animation
                plt.cla()
                im = plt.imshow(spins, animated=True, vmin=-1, vmax=1)
                plt.draw()
                plt.pause(0.00001)

        return spins

    else:
        print("Incorrect dynamics given, check your spelling?")