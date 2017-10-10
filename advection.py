import numpy as np
import matplotlib.pyplot as plt

class Grid:
    def __init__(self, zones, ng=2):
        self.a = np.zeros(zones + 2*ng)
        self.xmin = 0.0
        self.xmax = 1.0
        self.dx = (self.xmax - self.xmin) / zones
        self.x = (np.arange(zones + 2 * ng) - 0.5) * self.dx + self.xmin

        self.zones = zones
        self.ng = ng
        self.ilo = ng
        self.ihi = zones - 1 + ng

def initialize(grid):
    grid.a[:] = np.sin(2 * np.pi * grid.x)

def fill_gc(grid):
    grid.a[0:grid.ilo] = grid.a[grid.ihi+1-grid.ng:grid.ihi+1]
    grid.a[grid.ihi+1 : grid.ihi+1+grid.ng] = grid.a[grid.ilo : grid.ilo+grid.ng]

def evolve(grid, tmax, C=0.5, u=1.0):
    t = 0                 #init t
    dt = C * grid.dx / u      #cal dt

    while t < tmax:       #evolve while t less than tmax
        olda = grid.a.copy()
        for i in range(grid.ilo, grid.ihi+1):                #change values in array
            grid.a[i] = olda[i] - (C * (olda[i] - olda[i - 1]))
        t += dt
        fill_gc(grid)

    # show plots
        plt.clf()
        plt.plot(grid.x, grid.a)
        plt.axis([0, 1, -1, 1])
        plt.pause(0.0001)
        plt.draw()

def run():
    grid = Grid(32)

# show plots
    plt.ion()

    initialize(grid)
    fill_gc(grid)
    plt.plot(grid.x, grid.a)
    plt.draw()
    evolve(grid, 10.0)

run()
