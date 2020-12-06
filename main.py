import numpy as np
from solution import task
from task3 import task3


def f(x, y, t):
    return np.sin(np.pi * x / 2) * np.sin(np.pi * y) * np.cos(2 * t) * (4 - np.pi ** 2 * 5 / 4)


def phi(x, y):
    return np.sin(np.pi * x / 2) * np.sin(np.pi * y)


def ksi(x, y):
    return 0


if __name__ == '__main__':
    print("Hello")
    # task3(32, 0.0001)
    task(16, f=f, phi=phi, ksi=ksi, filename='resources/analyticSolveTest')
