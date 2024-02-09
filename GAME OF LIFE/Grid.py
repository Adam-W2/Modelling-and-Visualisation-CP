import numpy as np

class Grid:
    def __init__(self, N, P):
        self.prob = P
        self.rows = N
        self.columns = N
        self.grid_array = 0

    def create_random_grid(self):
        self.grid_array = np.random.choice([0, 1], size=(self.rows, self.columns), p=[1 - self.prob, self.prob])
        return self.grid_array

    def blinker(self):
        array = np.zeros((self.rows,self.columns))

        array[self.rows//2][self.columns//2] = 1
        array[self.rows//2 + 1][self.columns//2] = 1
        array[self.rows//2 - 1][self.columns//2] = 1

        self.grid_array = array
        return self.grid_array

    def glider(self):
        array = np.zeros((self.rows, self.columns))
        final = self.rows - 1
        for i in range(1,4):
            array[final - 1][final-i] = 1
        array[final-2][final-1] = 1
        array[final-3][final-2] = 1

        self.grid_array = array
        return self.grid_array

    def toad(self):
        array = np.zeros((self.rows, self.columns))
        for i in range(1,4):
            array[self.columns // 2][self.rows // 2 + i] = 1
            array[self.rows // 2 - 1][self.columns // 2 + i - 1] = 1

        self.grid_array = array
        return self.grid_array

    def lightship(self):
        array = np.zeros((self.rows, self.columns))
        for i in range(1,6):
            array[self.columns // 2][self.rows // 2 + i] = 1

        for i in range(1,3):
            array[self.columns // 2 - i][self.rows // 2 + 1] = 1

        array[self.columns // 2 - 3][self.rows // 2 + 2] = 1
        array[self.columns // 2 - 4][self.rows // 2 + 4] = 1
        array[self.columns // 2 - 1][self.rows // 2 + 6] = 1
        array[self.columns // 2 - 3][self.rows // 2 + 6] = 1

        self.grid_array = array
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

    def summing(self):
        return np.sum(self.grid_array)

    def get_neighbours(self, x, y):
        temp = 0
        for n in range(-1, 2):
            for m in range(-1, 2):
                x_edge = (x+n+self.rows) % self.rows
                y_edge = (y+m+self.columns) % self.columns
                temp += self.grid_array[x_edge][y_edge]
        temp -= self.grid_array[x][y]
        return temp