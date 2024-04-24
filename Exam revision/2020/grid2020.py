import matplotlib
matplotlib.use("TKAgg")
import matplotlib.pyplot as plt
import numpy as np
import random


class Grid:
    def __init__(self, N, P):
        self.prob = P
        self.rows = N
        self.columns = N
        self.grid_array = np.zeros((self.rows, self.columns), dtype=int)

    def create_random_grid(self):
        self.grid_array = np.random.choice([1,0], size=(self.rows, self.columns), p=[1/2,1/2])
        return self.grid_array

    def SIRS(self):
        for i in range(self.rows**2):
            x = random.randint(0,self.columns-1)
            y = random.randint(0,self.rows-1)

            state = self.grid_array[x][y]
            xlist,ylist = self.get_neighbours(x, y)

            r = random.random()

            if state == 1:

                if r < self.prob:
                    xnew = np.random.choice(xlist)
                    ynew = np.random.choice(ylist)
                    self.grid_array[xnew,ynew] = 1

                else:
                    self.grid_array[x][y] = 0

    def get_neighbours(self, x, y):
        tempx = []
        tempy = []
        ran = [1,-1]
        for n in ran:

            x_edge = (x+n+self.rows) % self.rows
            tempx.append(x_edge)

            y_edge = (y+n+self.columns) % self.columns
            tempy.append(y_edge)
        tempx.append(x)
        tempy.append(y)
        return tempx,tempy

    def update_grid(self):
        for _ in range(self.rows **2):
            self.SIRS()

    def animation(self,nsteps):
        for n in range(nsteps):

            self.update_grid()
            if n % 5 == 0:
                # show animation
                plt.cla()
                im = plt.imshow(self.grid_array, animated=True, vmin=-1, vmax=2)

                plt.draw()
                plt.pause(0.00001)