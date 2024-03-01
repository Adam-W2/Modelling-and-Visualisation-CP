import matplotlib
matplotlib.use("TKAgg")
import matplotlib.pyplot as plt
import numpy as np
import random


class Grid:
    def __init__(self, N, P1,P2,P3):
        self.prob1 = P1
        self.prob2 = P2
        self.prob3 = P3
        self.rows = N
        self.columns = N
        self.grid_array = np.zeros((self.rows, self.columns), dtype=int)

    def create_random_grid(self):
        self.grid_array = np.random.choice([1,0, -1], size=(self.rows, self.columns), p=[1/3,1/3,1/3])
        return self.grid_array

    def SIRS(self):

        x = random.randint(0,self.columns-1)
        y = random.randint(0,self.rows-1)

        state = self.grid_array[x][y]
        infected = self.get_neighbours(x, y)

        r = random.random()

        if state == 1 and infected:
            if r < self.prob1:
                self.grid_array[x][y] = 0

        elif state == 0:
            if r < self.prob2:
                self.grid_array[x][y] = -1

        else:
            if r < self.prob3:
                self.grid_array[x][y] = 1


    def summing(self):
        return np.sum(self.grid_array)


    def get_neighbours(self, x, y):
        temp = False
        ran = [1,-1]
        for n in ran:

            x_edge = (x+n+self.rows) % self.rows
            if self.grid_array[x_edge][y] == 0:
                temp = True

            y_edge = (y+n+self.columns) % self.columns
            if self.grid_array[x][y_edge] == 0:
                temp = True

        return temp

    def update_grid(self):
        for _ in range(self.rows **2):
            self.SIRS()

    def animation(self,nsteps):
        for n in range(nsteps):

            self.update_grid()
            if n % 5 == 0:
                # show animation
                plt.cla()
                im = plt.imshow(self.grid_array, animated=True, vmin=-1, vmax=1)
                plt.draw()
                plt.pause(0.00001)

    def measure_contour(self,nsteps):
        count = 0
        for n in range(nsteps):
            self.update_grid()
            if n >= 100:
                unique, counts = np.unique(self.grid_array, return_counts=True)
                if 0 in unique:
                    count += counts[1]

        if count != 0:
            avg = count/nsteps

        else:
            avg = count
        return avg