import numpy as np

class Grid:
    def __init__(self,dx, dt,N,F):

        self.dx = dx
        self.dt = dt
        self.rows = N
        self.columns = N
        self.grid_U = np.zeros((self.rows,self.columns))
        self.grid_V = np.zeros((self.rows,self.columns))
        self.D1 = 0.2
        self.D2 = 0.1
        self.k = 0.06
        self.F = F
        self.R = 20

    def create_U_grid(self):
        center_point = np.array((int(self.grid_U.shape[0] / 2.), int(self.grid_U.shape[1] / 2.)))
        points = np.argwhere(self.grid_U <= 1000)
        rsquare = np.sqrt(((points - center_point)**2).sum(axis=1).reshape((self.rows,self.columns)))

        lessR = (np.where(rsquare < self.R))
        moreR = (np.where(rsquare >= self.R))

        self.grid_U[lessR] = 0.5
        self.grid_U[moreR] = 1

        self.grid_U += np.random.uniform(-0.01,0.01,(self.rows,self.columns))

        return self.grid_U

    def create_V_grid(self):
        center_point = np.array((int(self.grid_V.shape[0] / 2.), int(self.grid_V.shape[1] / 2.)))
        points = np.argwhere(self.grid_V <= 1000)
        rsquare = np.sqrt(((points - center_point)**2).sum(axis=1).reshape((self.rows,self.columns)))

        lessR = (np.where(rsquare < self.R))
        moreR = (np.where(rsquare >= self.R))

        self.grid_V[lessR] = 0.25
        self.grid_V[moreR] = 0.01

        self.grid_V += np.random.uniform(-0.01,0.01,(self.rows,self.columns))

        return self.grid_V

    def steps(self):

        neighbours_U = (np.roll(self.grid_U, 1, axis = 0) + np.roll(self.grid_U, -1, axis=0) +
                        np.roll(self.grid_U, 1, axis=1) + np.roll(self.grid_U, -1,axis=1) - 4 * self.grid_U)

        self.grid_U += ((self.dt * self.D1) / (self.dx ** 2)) * neighbours_U - self.dt * self.grid_U * self.grid_V ** 2 \
                       + self.dt * self.F * (1 - self.grid_U)

        neighbours_V = (np.roll(self.grid_V, 1, axis = 0) + np.roll(self.grid_V, -1, axis=0) +
                        np.roll(self.grid_V, 1, axis=1) + np.roll(self.grid_V, -1,axis=1) - 4 * self.grid_V)

        self.grid_V += (self.dt * self.D2)/(self.dx**2) * neighbours_V + self.dt * self.grid_U * self.grid_V ** 2 \
                       - (self.F + self.k) * self.grid_V * self.dt