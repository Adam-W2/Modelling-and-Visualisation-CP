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

        neighbours = (np.roll(self.grid, 1, axis=2) + np.roll(self.grid, -1, axis=2) +
                      np.roll(self.grid, 1, axis=1) + np.roll(self.grid, -1,axis=1) +
                      np.roll(self.grid,1,axis=0) + np.roll(self.grid,-1,axis=0))

        self.grid = 1/6 * (neighbours + self.rho)

        self.grid[:,0,:] = 0
        self.grid[:,self.rows-1,:] = 0
        self.grid[:,:,0] = 0
        self.grid[:,:,self.rows-1] = 0

        sumnew = np.sum(self.grid)

        return sumold,sumnew
    def step_gauss(self):
        sumold = np.sum(self.grid)
        for i in range(len(self.grid)-1):
            for j in range(len(self.grid)-1):
                for k in range(len(self.grid)-1):
                    self.grid[i,j,k] = 1/6 * (self.grid[i,j+1,k] + self.grid[i,j-1,k] + self.grid[i+1,j,k] +
                                              self.grid[i-1,j,k] + self.grid[i,j,k+1] + self.grid[i,j,k-1] + self.rho[i,j,k])
        sumnew = np.sum(self.grid)
        return sumold,sumnew
    def efield(self):

        x = (np.roll(self.grid, 1, axis=2) - np.roll(self.grid, -1, axis=2))/2
        y = (np.roll(self.grid, 1, axis=1) - np.roll(self.grid, -1,axis=1))/2
        z = (np.roll(self.grid,1,axis=0) - np.roll(self.grid,-1,axis=0))/2
        return x[25,:,:],y[25,:,:],z[25,:,:]