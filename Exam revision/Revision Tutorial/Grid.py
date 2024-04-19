import numpy as np

class Grid:
    def __init__(self,sig,k,v,dt,phi_zero,N):
        self.phi_zero = phi_zero
        self.dx = 1
        self.dt = dt
        self.rows = N
        self.columns = N
        self.grid_phi = np.zeros((self.rows,self.columns))
        self.D = 1
        self.sig = sig
        self.k = k
        self.v = v
        self.vcalc = 0

    def velocity(self):
        x = np.arange(0,50,1)
        y = np.arange(0,50,1)

        xx,yy = np.meshgrid(x,y)
        self.vcalc = self.v * np.sin(2*np.pi * yy/self.rows)

    def create_phi_grid(self):
        self.grid_phi = self.phi_zero + np.random.uniform(-0.1,0.1,(self.rows,self.columns))
        return self.grid_phi

    def steps(self):
        center_point = np.array((int(self.grid_phi.shape[0] / 2.), int(self.grid_phi.shape[1] / 2.)))
        points = np.argwhere(self.grid_phi <= 1000)
        rsquare = ((points - center_point)**2).sum(axis=1).reshape((self.rows,self.columns))

        source = np.exp(-(rsquare/self.sig**2))

        neighbours_phi = (np.roll(self.grid_phi, 1,axis=0) + np.roll(self.grid_phi, -1, axis=0) +
                          np.roll(self.grid_phi, 1,axis=1) + np.roll(self.grid_phi, -1, axis=1) - 4 * self.grid_phi)

        self.grid_phi += self.D * self.dt/self.dx**2 * neighbours_phi + self.dt * source - self.k * self.dt * self.grid_phi

    def steps_Q5(self):
        center_point = np.array((int(self.grid_phi.shape[0] / 2.), int(self.grid_phi.shape[1] / 2.)))
        points = np.argwhere(self.grid_phi <= 1000)
        rsquare = ((points - center_point)**2).sum(axis=1).reshape((self.rows,self.columns))

        source = np.exp(-(rsquare/self.sig**2))

        neighbours_phi = (np.roll(self.grid_phi, 1,axis=0) + np.roll(self.grid_phi, -1, axis=0) +
                          np.roll(self.grid_phi, 1,axis=1) + np.roll(self.grid_phi, -1, axis=1) - 4 * self.grid_phi)

        self.grid_phi += self.D * self.dt/self.dx**2 * neighbours_phi + self.dt * source - self.k * self.dt * self.grid_phi - self.dt * self.vcalc * (np.roll(self.grid_phi,1,axis=1)-np.roll(self.grid_phi,-1,axis=1))/2