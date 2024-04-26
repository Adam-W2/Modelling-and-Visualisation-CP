import numpy as np

class Grid:
    def __init__(self,dx, dt,N):
        self.dx = dx
        self.dt = dt
        self.rows = N
        self.columns = N
        self.grid_a = np.zeros((self.rows,self.columns))
        self.grid_b = np.zeros((self.rows,self.columns))
        self.grid_c = np.zeros((self.rows,self.columns))
        self.grid_t = np.zeros((self.rows,self.columns))
        self.q = 1
        self.p = 2.5
        self.D = 0.5

    def create_random_grid(self,grid):
        grid += np.random.uniform(0,1/3,(self.rows,self.columns))
        return grid

    def steps(self):
        minus = 1 - self.grid_c - self.grid_b - self.grid_a

        neighbours_c = (np.roll(self.grid_c, 1, axis = 0) + np.roll(self.grid_c, -1, axis=0) +
                        np.roll(self.grid_c, 1, axis=1) + np.roll(self.grid_c, -1,axis=1) - 4 * self.grid_c)

        self.grid_c += self.D * self.dt * neighbours_c + self.dt * self.q * self.grid_c * (1 - self.grid_a - self.grid_b - self.grid_c) - self.dt * self.p * self.grid_b * self.grid_c

        neighbours_a = (np.roll(self.grid_a, 1, axis=0) + np.roll(self.grid_a, -1, axis=0) +
                        np.roll(self.grid_a, 1, axis = 1) + np.roll(self.grid_a, -1, axis = 1) - 4 * self.grid_a)

        self.grid_a += self.D * self.dt * neighbours_a + self.dt * self.q * self.grid_a * (1 - self.grid_a - self.grid_b - self.grid_c) - self.dt * self.p * self.grid_a * self.grid_c

        neighbours_b = (np.roll(self.grid_b, 1, axis = 0) + np.roll(self.grid_b, -1, axis=0) +
                        np.roll(self.grid_b, 1, axis=1) + np.roll(self.grid_b, -1,axis=1) - 4 * self.grid_b)

        self.grid_b += self.D * self.dt * neighbours_b + self.dt * self.q * self.grid_b * (1 - self.grid_a - self.grid_b - self.grid_c) - self.dt * self.p * self.grid_a * self.grid_b



    def update_t(self):
        minus = 1 - self.grid_b - self.grid_c - self.grid_a
        # Stack the input arrays along a new axis to compare element-wise
        stacked_arrays = np.stack((self.grid_a, self.grid_b, self.grid_c,minus), axis=0)

        # Find the index of the maximum value at each coordinate
        max_indices = np.argmax(stacked_arrays, axis=0)

        # Create masks for each input array
        mask_arr1 = (max_indices == 0)
        mask_arr2 = (max_indices == 1)
        mask_arr3 = (max_indices == 2)
        mask_arr4 = (max_indices == 3)

        # Set values in the fourth array based on the masks
        self.grid_t[mask_arr1] = 1
        self.grid_t[mask_arr2] = 2
        self.grid_t[mask_arr3] = 3
        self.grid_t[mask_arr4] = 0
