import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
import math


# Gaussian function
def gauss(x, y, sigmaX, sigmaY, A):
    return A * math.exp(-(x ** 2 / (2 * sigmaX ** 2) + y ** 2 / (2 * sigmaY ** 2)))


# Update function for animation
def update_graph(num, data, graph):
    eps = 0.001
    neighbourhood_factor = 0.03
    for index in range(len(data[2])):
        data[0][index] += np.random.uniform(low=-0.001, high=0.001)
        data[1][index] += np.random.uniform(low=-0.001, high=0.001)
        data[2][index] += gauss(data[0][index], data[1][index], 0.3, 0.3, 0.005)

        x, y, z = 0, 0, 0
        for other_index in range(len(data[0])):
            if abs(data[0][other_index] - data[0][index]) < eps and abs(
                    data[1][other_index] - data[1][index]) < eps and abs(data[2][other_index] - data[2][index]) < eps:
                x += data[0][other_index]
                y += data[1][other_index]
                z += data[2][other_index]

        data[0][index] += neighbourhood_factor * x
        data[1][index] += neighbourhood_factor * y
        data[2][index] += neighbourhood_factor * z

    graph._offsets3d = (data[0], data[1], data[2])
    return graph,


# Initialize the plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
title = ax.set_title('3D Point Movement')

# Initialize data
number_points = 2000
data = [[], [], []]
for _ in range(number_points):
    x = np.random.uniform(low=-1, high=1)
    y = np.random.uniform(low=-1, high=1)
    if x ** 2 + y ** 2 <= 1:
        data[0].append(x)
        data[1].append(y)
        data[2].append(0)

# Scatter plot
graph = ax.scatter(data[0], data[1], data[2], s=5, marker='o')

# Animate
ani = animation.FuncAnimation(fig, update_graph, fargs=(data, graph), frames=600, interval=50, blit=False)

plt.show()
