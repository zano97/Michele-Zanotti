from pylab import *
import numpy as np
from numpy import random as rn
from imagesc import imagesc




nstep = 50
noutput = [10, 20, 40, 50]
N = int(800)
KT = 1.0
H = 0.0
J = 1.0
JdivKT = J/KT
HdivKT = H/KT
# Initial random spin configuration
spins = randint(1, 3, size=(N, N))*2-3
# Half matrix of sites for spin change
halflattice = zeros((N, N), float)
a = range(0, N, 2)
b = range(1, N, 2)
for i in range(0, N, 2):
    halflattice[i][a] = 1
    halflattice[i+1][b] = 1
# Let's evolve the system
for k in range(1, nstep):
    sumneighbors = np.roll(spins, 1, axis=1) + np.roll(spins, -1, axis=1) + np.roll(spins, 1, axis=0) + np.roll(spins, -1, axis=0)
    deltaEdivKT = -spins*(JdivKT*sumneighbors+HdivKT)
    prob = exp(deltaEdivKT)
    randomatrix = rn.rand(N, N)
    changespin = -2*randomatrix*(halflattice+1)
    spins = spins*changespin
    halflattice = 1 - halflattice
    k = k + 1
print(spins)


