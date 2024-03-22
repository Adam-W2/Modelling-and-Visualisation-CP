import numpy as np

class Grid:
    def __init__(self,N):

        self.rows = N
        self.columns = N
        self.grid = np.zeros((self.rows,self.columns,self.rows))
        self.rho = np.zeros((self.rows,self.columns,self.rows))

    def initialrho(self):
        self.rho[int(self.rows/2),int(self.columns/2),int(self.rows/2)] = 1

    def steps(self):

        sumold = np.sum(self.grid)

        neighbours = (np.roll(self.grid, (1, 0,0), (1, 0,0)) + np.roll(self.grid, (-1, 0,0), (1, 0,0)) +
                      np.roll(self.grid, (0, 1,0), (0, -1,0)) + np.roll(self.grid, (0, -1,0),(0, -1,0)) +
                      np.roll(self.grid,(1,0,0),(0,-1,0)) + np.roll(self.grid,(-1,0,0),(0,-1,0)))

        self.grid = 1/6 * (neighbours + self.rho)

        self.grid[:,0,:] = 0
        self.grid[:,self.rows-1,:] = 0
        self.grid[:,:,0] = 0
        self.grid[:,:,self.rows-1] = 0

        sumnew = np.sum(self.grid)

        return sumold,sumnew

    def efield(self):
        x = (np.roll(self.grid, (1, 0,0), (1, 0,0)) - np.roll(self.grid, (-1, 0,0), (1, 0,0)))/2
        y = (np.roll(self.grid, (0, 1,0), (0, -1,0)) - np.roll(self.grid, (0, -1,0),(0, -1,0)))/2
        z = (np.roll(self.grid,(1,0,0),(0,-1,0)) - np.roll(self.grid,(-1,0,0),(0,-1,0)))/2
        E = - (x + y + z)
        return E,-x[25,:,:],-y[25,:,:],-z[50,:,:]