"""
    Автор: Орел Максим
    Группа: КБ-161
    Вариант: 11
    Дата создания: 2/05/2018
    Python Version: 3.6
"""
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from scipy.interpolate import interp1d

# Constants
accuracy = 0.00001
START_X = -1
END_X = 3
START_Y = -2
END_Y = 4

x = [0.0, 0.3, 0.6, 0.9, 1.2, 1.5, 1.8, 2.1, 2.4, 2.7]
y = [-1.0, 0.1, 1.3, 1.7, 0.3, 0.7, 2.5, 3.0, 2.9, 2.7]


def build_points(x_array, y_array):
    for i in range(0, len(x_array)):
        plt.scatter(x_array[i], y_array[i])


def calc_y(a0, a1, a2, point, xi):
    return a0 + a1 * (point - xi) + a2 * (point - xi) ** 2


if __name__ == "__main__":

    try:
        build_points(x, y)

        a0 = y

        a1 = [(y[1] - y[0]) / (y[1] - y[0])]
        for i in range(0, len(x) - 1):
            a1.append(2 * (y[i + 1] - y[i]) / (x[i + 1] - x[i]) - a1[i])

        a2 = []
        for i in range(0, len(x) - 1):
            a2.append((a1[i + 1] - a1[i]) / (2 * (x[i + 1] - x[i])))

        for i in range(0, len(x) - 1):
            point = np.linspace(x[i], x[i + 1])
            plt.plot(point, calc_y(a0[i], a1[i], a2[i], point, x[i]))

        plt.xlabel('X')
        plt.ylabel('Y')
        plt.grid()
        plt.show()

        # # Variant 2
        # build_points(x, y)
        #
        # new_length = 100
        # new_x = np.linspace(min(x), max(x), new_length)
        # new_y = sp.interpolate.interp1d(x, y, kind='cubic')(new_x)
        #
        # plt.plot(new_x, new_y)
        #
        # plt.grid(True)
        # plt.axis([START_X, END_X, START_Y, END_Y])
        # plt.axhline(y=0, color='k')
        # plt.axvline(x=0, color='k')
        # plt.show()

    except Exception as e:
        print(e)
