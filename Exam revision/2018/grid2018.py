import numpy as np

class Grid:
    def __init__(self,dx, dt,X,Y,R):
        self.dx = dx
        self.dt = dt
        self.rows = Y
        self.columns = X
        self.grid_mu = np.zeros(self.columns)
        self.R = R
        self.D = 1
        self.a = 1

    def create_mu_grid(self):
        center_point = np.array((int(self.grid_mu.shape[0] / 2.), int(self.grid_mu.shape[1] / 2.)))
        points = np.argwhere(self.grid_mu <= 1000)
        rsquare = np.sqrt(((points - center_point)**2).sum(axis=1).reshape((self.rows,self.columns)))

        lessR = (np.where(rsquare < self.R))
        moreR = (np.where(rsquare >= self.R))

        self.grid_mu[lessR] = 1
        self.grid_mu[moreR] = 0

        return self.grid_mu

    def create_mu_grid_1D(self):
        points = np.argwhere(self.grid_mu <= 1000)
        rsquare = np.sqrt(((points - [0])**2).sum(axis=1).reshape((self.rows,self.columns)))

        lessR = (np.where(rsquare <= self.columns/10))
        self.grid_mu[lessR[1]] = 1

        print(self.grid_mu)
        return self.grid_mu

    def steps(self):

        neighbours_mu = (np.roll(self.grid_mu, 1, axis = 0) + np.roll(self.grid_mu, -1, axis=0) +
                         np.roll(self.grid_mu, 1, axis=1) + np.roll(self.grid_mu, -1,axis=1) - 4 * self.grid_mu)

        self.grid_mu += self.D * self.dt * neighbours_mu + self.dt * self.a * self.grid_mu * (1 - self.grid_mu)

    def steps_1D(self):
        neighbours_mu = (np.roll(self.grid_mu, 1, axis = 0) + np.roll(self.grid_mu, -1, axis=0) - 2*self.grid_mu)

        self.grid_mu += self.D * self.dt * neighbours_mu + self.dt * self.a * self.grid_mu * (1 - self.grid_mu)
        self.grid_mu[0] = 1
        self.grid_mu[self.columns - 1] = self.grid_mu[self.columns - 2]