import numpy as np
import matplotlib.pyplot as plt

class Grid:
    def __init__(self, zones, ng=1):
        self.a = np.zeros(zones + 2*ng)
        self.xmin = 0.0
        self.xmax = 1.0
        self.dx = (self.xmax - self.xmin)/zones
        self.x = (np.arange(zones + 2) - 0.5)*self.dx + self.xmin

        self.zones = zones
        self.ng = ng
        self.ilo = ng
        self.ihi = zones - 1 + ng

def initialize(grid):
    grid.a[:] = np.sin(2*np.pi*grid.x)

def fill_gc(grid):
    grid.a[0:grid.ilo] = grid.a[grid.ihi+1-grid.ng:grid.ihi+1]
    grid.a[grid.ihi+1:grid.ihi+1+grid.ng] = grid.a[grid.ilo:grid.ilo+grid.ng]

def evolve(grid, tmax, C=0.9, u=1.0):
    t = 0
    dt = C*grid.dx/u

    while t < tmax:
        olda = grid.a.copy()
        for i in range(grid.ilo, grid.ihi+1):
            grid.a[i] = olda[i] - (C * (olda[i] - olda[i - 1]))
        t += dt
        fill_gc(grid)
        plt.clf()
        plt.plot(grid.x, grid.a)
        plt.pause(0.001)
        plt.draw()
#        print(t, grid)

def run():
    #data = [1, 4, 9, 4, 1]
    grid = Grid(32)

    plt.ion()

    initialize(grid)
    fill_gc(grid)
    plt.plot(grid.x, grid.a)
    plt.draw()
    evolve(grid, 10.0)

run()
