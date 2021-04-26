import math
import cmath
import numpy as np
import matplotlib.pyplot as plot
import sympy
from sympy import pretty
from sympy.abc import pi


if __name__ == '__main__':

    #make pairs
    ax = []
    ay = []
    bx = []
    by = []

    circle_points = [0, 0, 0, 0] #area of points generated inside circle

    for i in range(4):
        x = np.random.uniform(0, 1, 10 ** (i+3))
        y = np.random.uniform(0, 1, 10 ** (i+3))
        dist = np.sqrt(np.square(x) + np.square(y))  # euclian distance
        for j in range(10 ** (i+3)):
            if dist[j] < 1: #check if eucliean < 1 if yes, inc #of points inside circle
                circle_points[i] = circle_points[i] + 1
                ax.append(x[j])
                ay.append(y[j])
            else: #else, inc other
                bx.append(x[j])
                by.append(y[j])
            # add to plot with colors
        plot.figure(i)
        plot.scatter(ax, ay, c="blue", s=1)
        plot.scatter(bx, by, c="red", s=1)
        ax.clear()
        ay.clear()
        bx.clear()
        by.clear()
        # label

    #print statements for lab
    pie = 4 * (circle_points[0] / 10 ** 3) #4 * #ofpoints genrated inside circle/ #of points inside square
    print("n = 10 ^ 3  pi =", pie, " error = ", '{0:.4f}'.format(np.absolute((np.pi - pie) / np.pi) * 100), "%")
    pie = 4 * (circle_points[1] / 10 ** 4)
    print("n = 10 ^ 4  pi =", pie, " error = ", '{0:.4f}'.format(np.absolute((np.pi - pie) / np.pi) * 100), "%")
    pie = 4 * (circle_points[2] / 10 ** 5)
    print("n = 10 ^ 5  pi =", pie, " error = ", '{0:.4f}'.format(np.absolute((np.pi - pie) / np.pi) * 100), "%")
    pie = 4 * (circle_points[3] / 10 ** 6)
    print("n = 10 ^ 6  pi =", pie, " error = ", '{0:.4f}'.format(np.absolute((np.pi - pie) / np.pi) * 100), "%")

    plot.xlabel("Figure 1: Estimating " + pretty(pi) + " using simulation")
    plot.show()