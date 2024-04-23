import numpy as np

class Grid:
    def __init__(self,dx, dt,phi_zero,N,alpha):
        self.phi_zero = phi_zero
        self.dx = dx
        self.dt = dt
        self.rows = N
        self.columns = N
        self.grid_phi = np.zeros((self.rows,self.columns))
        self.grid_mew = np.zeros((self.rows,self.columns))
        self.grid_M = np.zeros((self.rows,self.columns))
        self.M = 0.1
        self.a = 0.1
        self.X = 0.3
        self.K = 0.1
        self.D = 1
        self.c = 0.1
        self.alpha = alpha
        self.phibar = 0.5

    def create_phi_grid(self):
        self.grid_phi = self.phi_zero + np.random.uniform(-0.01,0.01,(self.rows,self.columns))
        return self.grid_phi

    def create_M_grid(self):
        self.grid_M += np.random.uniform(-0.01, 0.01, (self.rows, self.columns))
        return self.grid_M

    def steps(self):

        neighbours_mew = (np.roll(self.grid_phi, 1, axis=0) + np.roll(self.grid_phi, -1, axis=0) +
                          np.roll(self.grid_phi, 1, axis = 1) + np.roll(self.grid_phi, -1, axis = 1) - 4 * self.grid_phi)

        self.grid_mew = - self.a * self.grid_phi + self.a * (self.grid_phi) ** 3 - (self.X/2) * self.grid_M**2 - self.K / (self.dx ** 2) * neighbours_mew

        neighbours_phi = (np.roll(self.grid_mew, 1, axis = 0) + np.roll(self.grid_mew, -1, axis=0) +
                          np.roll(self.grid_mew, 1, axis=1) + np.roll(self.grid_mew, -1,axis=1) - 4 * self.grid_mew)

        self.grid_phi += ((self.dt * self.M) / (self.dx ** 2)) * neighbours_phi

        neighbours_M = (np.roll(self.grid_M, 1, axis = 0) + np.roll(self.grid_M, -1, axis=0) +
                        np.roll(self.grid_M, 1, axis=1) + np.roll(self.grid_M, -1,axis=1) - 4 * self.grid_M)

        self.grid_M += (self.dt * self.D)/(self.dx**2) * neighbours_M - self.dt * ((self.c - self.X*self.grid_phi)*self.grid_M + self.c * self.grid_M**3)

    def steps_new(self):

        neighbours_mew = (np.roll(self.grid_phi, 1, axis=0) + np.roll(self.grid_phi, -1, axis=0) +
                          np.roll(self.grid_phi, 1, axis = 1) + np.roll(self.grid_phi, -1, axis = 1) - 4 * self.grid_phi)

        self.grid_mew = - self.a * self.grid_phi + self.a * (self.grid_phi) ** 3 - (self.X/2) * self.grid_M**2 - self.K / (self.dx ** 2) * neighbours_mew

        neighbours_phi = (np.roll(self.grid_mew, 1, axis = 0) + np.roll(self.grid_mew, -1, axis=0) +
                          np.roll(self.grid_mew, 1, axis=1) + np.roll(self.grid_mew, -1,axis=1) - 4 * self.grid_mew)

        self.grid_phi += ((self.dt * self.M) / (self.dx ** 2)) * neighbours_phi - self.alpha * (self.grid_phi - self.phibar)

        neighbours_M = (np.roll(self.grid_M, 1, axis = 0) + np.roll(self.grid_M, -1, axis=0) +
                        np.roll(self.grid_M, 1, axis=1) + np.roll(self.grid_M, -1,axis=1) - 4 * self.grid_M)

        self.grid_M += (self.dt * self.D)/(self.dx**2) * neighbours_M - self.dt * ((self.c - self.X*self.grid_phi)*self.grid_M + self.c * self.grid_M**3)
