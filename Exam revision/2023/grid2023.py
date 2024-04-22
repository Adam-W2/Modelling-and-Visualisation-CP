import numpy as np
import random

class Grid:
    def __init__(self, N,prob2,prob3):
        self.prob = 0
        self.rows = N
        self.columns = N
        self.grid_array = np.zeros((self.rows, self.columns), dtype=int)
        self.size = N
        self.prob1 = 0.5
        self.prob2 = prob2
        self.prob3 = prob3

    def generate_pie_array(self):
        # Define the number of pie slices for each value (0, 1, 2)
        slices_per_value = self.size // 3

        # Calculate the radius of the pie
        radius = self.size // 2

        # Calculate the angle per wedge
        angle_per_wedge = 2 * np.pi / 3

        for i in range(self.size):
            for j in range(self.size):
                # Calculate the distance from the center
                distance_from_center = np.sqrt((i - radius) ** 2 + (j - radius) ** 2)

                # Calculate the angle from the center
                angle = np.arctan2(j - radius, i - radius)
                if angle < 0:
                    angle += 2 * np.pi

                # Determine the value based on the angle
                if angle < angle_per_wedge:
                    self.grid_array[i, j] = 0
                elif angle < 2 * angle_per_wedge:
                    self.grid_array[i, j] = 1
                else:
                    self.grid_array[i, j] = 2

    def create_random_grid(self):
        self.grid_array = np.random.choice([0, 1,2], size=(self.rows, self.columns), p=[1/3,1/3,1/3])
        return self.grid_array

    def step(self):
        next_state = np.zeros_like(self.grid_array)

        for x in range(self.rows):
            for y in range(self.columns):
                state = self.grid_array[x][y]
                neighbours = self.get_neighbours(x, y)

                if state == 0 and neighbours[1] >= 3:
                    next_state[x][y] = 1
                elif state == 1 and neighbours[2] >= 3:
                    next_state[x][y] = 2
                elif state == 2 and neighbours[0] >= 3:
                    next_state[x][y] = 0
                else:
                    next_state[x][y] = state

        self.grid_array = next_state

    def step_sto(self):
        for i in range(self.rows**2):
            x = random.randint(0, self.columns - 1)
            y = random.randint(0, self.rows - 1)

            state = self.grid_array[x][y]
            neighbours = self.get_neighbours(x, y)

            r = random.random()

            if state == 0 and neighbours[1] >= 1:
                if r < self.prob1:
                    self.grid_array[x][y] = 1

            elif state == 1 and neighbours[2] >= 1:
                if r < self.prob2:
                    self.grid_array[x][y] = 2

            elif state == 2 and neighbours[0] >= 1:
                if r < self.prob3:
                    self.grid_array[x][y] = 0

    def summing(self):
        return np.sum(self.grid_array)

    def get_neighbours(self, x, y):
        temp = [0,0,0]
        for n in range(-1, 2):
            for m in range(-1, 2):
                if n != x and m != y:
                    x_edge = (x+n+self.rows) % self.rows
                    y_edge = (y+m+self.columns) % self.columns
                    if self.grid_array[x_edge,y_edge] == 0:
                        temp[0] += 1
                    elif self.grid_array[x_edge,y_edge] == 1:
                        temp[1] += 1
                    else:
                        temp[2] += 1
        return temp