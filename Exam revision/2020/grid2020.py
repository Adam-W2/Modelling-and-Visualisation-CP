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

    def create_one_grid(self):
        x = random.randint(0, self.columns - 1)
        y = random.randint(0, self.rows - 1)
        self.grid_array[x][y] = 1

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

    def jacknife(self,L):

        n = len(L)
        jacknife_estimate = np.zeros(n)

        # Loop over length of input list
        for i in range(n):
            # Create new list and remove ith component
            sample = np.delete(L, i)

            # Create squared version list and calculate specific heat, appending to masterlist
            sample2 = np.square(sample)

            samplemean = sample.mean()
            sample2mean = sample2.mean()
            jacknife_estimate[i] = (sample2mean - samplemean**2)/self.rows**2

        # Create squared specific heat list and calcuate averages
        jacknife_estimate2 = np.square(jacknife_estimate)
        c = jacknife_estimate.mean()
        c2 = jacknife_estimate2.mean()

        # Calculate errors
        error = np.sqrt(c2 - c ** 2) * np.sqrt(len(L))
        return error