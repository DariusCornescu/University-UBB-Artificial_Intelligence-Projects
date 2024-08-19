import matplotlib.pyplot as plt
import numpy as np

# Function to estimate pi using points in 2D
def compute_pi(n):
    cc = 0
    for i in range(n):
        x = np.random.uniform(low=-1, high=1)
        y = np.random.uniform(low=-1, high=1)
        if x**2 + y**2 <= 1:
            cc += 1
    return cc / n * 4

# Function to estimate pi using points in 3D
def compute_pi_3d(n):
    cc = 0
    for i in range(n):
        x = np.random.uniform(low=-1, high=1)
        y = np.random.uniform(low=-1, high=1)
        z = np.random.uniform(low=-1, high=1)
        if x**2 + y**2 + z**2 <= 1:
            cc += 1
    return cc / n * 6

# Function to plot the convergence of pi estimation in 2D
def n_graph():
    x = []
    y = []
    for n in range(1000, 50000, 50):
        x.append(n)
        y.append(compute_pi(n))
    plt.scatter(x, y)
    plt.axhline(y=np.pi, color='r', linestyle='-')
    plt.xlabel('Number of points')
    plt.ylabel('Estimated Pi')
    plt.title('Convergence of Pi estimation in 2D')
    plt.show()

# Function to plot the convergence of pi estimation in 3D
def n_graph_3d():
    x = []
    y = []
    for n in range(1000, 50, 50):
        x.append(n)
        y.append(compute_pi_3d(n))
    plt.scatter(x, y)
    plt.axhline(y=np.pi, color='r', linestyle='-')
    plt.xlabel('Number of points')
    plt.ylabel('Estimated Pi')
    plt.title('Convergence of Pi estimation in 3D')
    plt.show()

n_graph()
n_graph_3d()
