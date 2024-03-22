import numpy as np

class Grid:
    def __init__(self,dx, dt,phi_zero,N):
        self.phi_zero = phi_zero
        self.dx = dx
        self.dt = dt
        self.rows = N
        self.columns = N
        self.grid_phi = np.zeros((self.rows,self.columns))
        self.grid_mew = np.zeros((self.rows,self.columns))
        self.M = 0.1
        self.a = 0.1
        self.b = 0.1
        self.K = 0.1

    def create_phi_grid(self):
        self.grid_phi = self.phi_zero + np.random.uniform(-0.1,0.1,(self.rows,self.columns))
        return self.grid_phi


    def steps(self):

        neighbours_mew = (np.roll(self.grid_phi, (1, 0), (1, 0)) + np.roll(self.grid_phi, (-1, 0), (1, 0)) +
                          np.roll(self.grid_phi, (1, 0), (0, 1)) + np.roll(self.grid_phi, (-1, 0),(0, 1)) - 4 * self.grid_phi)

        self.grid_mew = - self.a * self.grid_phi + self.b * (self.grid_phi) ** 3 - self.K / (self.dx ** 2) * neighbours_mew

        neighbours_phi = (np.roll(self.grid_mew, (1, 0), (1, 0)) + np.roll(self.grid_mew, (-1, 0), (1, 0)) +
                          np.roll(self.grid_mew, (1, 0), (0, 1)) + np.roll(self.grid_mew, (-1, 0),(0, 1)) - 4 * self.grid_mew)

        self.grid_phi += (self.dt * self.M)/(self.dx**2) * neighbours_phi

    def free_energy(self):
        grad1 = ((np.roll(self.grid_phi, (1, 0), (1, 0)) - np.roll(self.grid_phi, (-1, 0), (1, 0)))/(2 * self.dx)) ** 2
        grad2 = ((np.roll(self.grid_phi, (1, 0), (0, 1)) - np.roll(self.grid_phi, (-1, 0), (0, 1)))/(2 * self.dx)) ** 2
        free = - (self.a/2) * (self.grid_phi ** 2) + (self.a/4) * (self.grid_phi ** 4) + (self.K/2) * (grad1 + grad2)
        return np.sum(free)

