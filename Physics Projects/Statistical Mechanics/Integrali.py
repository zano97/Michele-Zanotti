from matplotlib import pylab
from pylab import *
from pylab import plot as plt
from sympy import *

# Symbolic Solution
u = symbols('u')
f = (sin(10 * u) + cos(50 * u)) ** 2
g = integrate(f)
fint = float(g.subs(u, 1))
print("Real value: " + str(fint))

# Convert to Python function
fun = lambdify(u, f, "numpy")


# Plotting
xx = linspace(0, 1, 10000)
yy = fun(xx)
plt(xx, yy)

# Calculating using Monte Carlo hit or miss algorithm
fmax = 4.0  # Upper limit of f(x) for x (0,1)
N = 10000
hit = 0.
intest = zeros(N, 1)
plt(xx, yy, '-g')
for i in range(1, N):
    x = rand(1)
    y = rand(1)*fmax
    if y < fun(x):
        hit = hit + 1
        plt(x, y, '.r')
    else:
        plt(x, y, '.b')
    intest[i] = hit/i*fmax
show()
plt(array(range(0, N)), intest, '-r')
plt(array(range(0, N)), np.full(N, fint), '-b')
xlabel('i')
ylabel('I')
show()
errore = float(1/sqrt(N))
delta = fint - intest[N-1]
print("Estimation through Monte Carlo hit or miss: " + str(intest[N-1]) + " +- " + str(errore) + "\n"
      "Difference between the two: " + str(delta))
