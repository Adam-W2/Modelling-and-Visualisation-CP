import numpy as np

class Grid:
    def __init__(self, N):
        self.rows = N
        self.columns = N
        self.grid_array = np.random.choice([0, 1], size=(self.rows, self.columns), p=[1 - 0.3, 0.3])

    def create_grid(self):
        return self.grid_array

    def conways_game(self):
        next_state = np.zeros_like(self.grid_array)

        for x in range(self.rows):
            for y in range(self.columns):
                state = self.grid_array[x][y]
                neighbours = self.get_neighbours(x, y)

                if state == 0 and neighbours == 3:
                    next_state[x][y] = 1
                elif state == 1 and (neighbours < 2 or neighbours > 3):
                    next_state[x][y] = 0
                else:
                    next_state[x][y] = state

        self.grid_array = next_state

    def get_neighbours(self, x, y):
        temp = 0
        for n in range(-1, 2):
            for m in range(-1, 2):
                x_edge = (x+n+self.rows) % self.rows
                y_edge = (y+m+self.columns) % self.columns
                temp += self.grid_array[x_edge][y_edge]
        temp -= self.grid_array[x][y]
        return temp