import math
import numpy as np
import matplotlib.pyplot as plt


def calculate_error(pi_prime):
    return np.round(np.absolute((np.pi - pi) / np.pi) * 100, 4)


if __name__ == '__main__':
    x = np.random.uniform(0, 1, 10 ** 6)
    y = np.random.uniform(0, 1, 10 ** 6)
    distance = np.sqrt(np.square(x) + np.square(y))

    # x and yt values for plotting the graph thing
    ax = []
    ay = []
    sx = []
    sy = []
    # number of points in the circle
    a = 0

    # n = 10**3
    for i in range(0, 10 ** 3):
        if distance[i] < 1:
            a += 1
            ax.append(x[i])
            ay.append(y[i])
        else:
            sx.append(x[i])
            sy.append(y[i])
    pi = (a / 10 ** 3) * 4
    print("\n n = 10 ^ 3  pi =", pi, " error = ", calculate_error(pi), "%")

    # n = 10**4
    for i in range(10 ** 3 + 1, 10 ** 4):
        if distance[i] < 1:
            a += 1
            ax.append(x[i])
            ay.append(y[i])
        else:
            sx.append(x[i])
            sy.append(y[i])
    pi = (a / 10 ** 4) * 4
    print(" n = 10 ^ 4  pi =", pi, " error = ", calculate_error(pi), "%")

    # n = 10**5, 10**6
    for n in range(5, 7):
        for i in range(10 ** (n - 1) + 1, 10 ** (n)):
            if distance[i] < 1:
                a += 1
        pi = (a / 10 ** n) * 4
        print(" n = 10 ^", n, "pi =", pi, " error = ", calculate_error(pi), "%")

    plt.scatter(ax, ay, c="blue", s=1)
    plt.scatter(sx, sy, c="red", s=1)
    plt.title("\nEstimating pi using simulation")
    plt