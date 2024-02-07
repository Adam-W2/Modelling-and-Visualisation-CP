import matplotlib
matplotlib.use("TKAgg")
import matplotlib.pyplot as plt
from Grid import Grid

N = 50
nsteps = 10000
grid = Grid(N)
grid.create_grid()

for n in range(nsteps):
    grid.conways_game()
    # show animation
    plt.cla()
    im = plt.imshow(grid.grid_array,animated=True,vmin=0,vmax=1)
    plt.draw()
    plt.pause(0.0001)
    if n % 10 == 0:
        print(n)
