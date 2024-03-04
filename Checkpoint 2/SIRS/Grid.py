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

        elif state == -1:
            if r < self.prob3:
                self.grid_array[x][y] = 1


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
                im = plt.imshow(self.grid_array, animated=True, vmin=-1, vmax=2)

                plt.draw()
                plt.pause(0.00001)

    def measure_contour(self,nsteps,which):
        count = []
        if which == "set":
            count_sqr = []
        for n in range(nsteps):
            self.update_grid()
            if n >= 100:
                unique, counts = np.unique(self.grid_array, return_counts=True)

                if 0 in unique:
                    unique_list = unique.tolist()
                    index = unique_list.index(0)
                    count.append(counts[index])
                    if which == "set":
                        count_sqr.append(counts[index] **2)
        if len(count) != 0:

            avg = sum(count)/len(count)
            if which == "set":
                error = self.bootstrap(count,self.calc_I)
                avg2 = sum(count_sqr)/len(count_sqr)

        else:
            avg = 0
            if which == "set":
                error = 0
                avg2 = 0
        if which == "set":
            return avg,avg2,error
        else:
            return avg

    def calc_I(self,I1,I2):
        # Calcualte the susepectibility
        x = (I2 - np.power(I1,2)) / (self.rows**2)
        return x

    def bootstrap(self,L,func):

        masterlist = []

        # Set number of k sets you want to resample
        for n in range(1000):
            sidelist1 = []
            sidelist2 = []

            # Loop over length of input list and extract random values, appending to list
            for i in range(len(L)):
                val = L[np.random.randint(0,len(L))]

                # Calculate the squared version and append
                val2 = val ** 2

                sidelist1.append(val)
                sidelist2.append(val2)

            # Calcute averages for both lists
            A = sum(sidelist1) / len(sidelist1)
            B = sum(sidelist2) / len(sidelist2)
            masterlist.append(func(A,B))

        # Create squared list and calulate averages for specific heat
        masterlist2 = [n ** 2 for n in masterlist]
        c = sum(masterlist) / len(masterlist)
        c2 = sum(masterlist2) / len(masterlist2)

        # Calculate error
        error = np.sqrt(c2 - c ** 2)
        return error

    def add_immune_cells(self, percentage_immune):
        num_immune_cells = int(self.rows * self.columns * percentage_immune)
        immune_indices = np.random.choice(range(self.rows * self.columns), size=num_immune_cells, replace=False)
        immune_coords = np.unravel_index(immune_indices, (self.rows, self.columns))
        for i in range(len(immune_coords[0])):
            x = immune_coords[0][i]
            y = immune_coords[1][i]
            self.grid_array[x,y] = 2


