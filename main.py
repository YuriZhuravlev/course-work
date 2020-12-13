import numpy as np
from solution import task, check_error
from task3 import task3


def f(x, y, t):
    # return np.sin(np.pi * x / 2) * np.sin(np.pi * y) * np.cos(2 * t)
    # return np.sin(np.pi * x / 2) * np.sin(np.pi * y) * np.cos(t)
    # return 5*np.sin(np.pi * x / 2) * np.sin(2 * np.pi * y) * np.cos(2 * t)
    return np.exp(x*y)*np.sin(np.pi * x / 2) * np.sin(np.pi * y) * np.cos(2 * t)
    # return (np.sin(np.pi * x / 2) + np.sin(np.pi * y)) * np.cos(2 * t)


def phi(x, y):
    # return np.sin(np.pi * x / 2) * np.sin(np.pi * y)
    return 0
    # return np.sin(np.pi * x / 2) * np.sin(np.pi * y)

def ksi(x, y):
    return 0
    # return np.sin(np.pi * x / 2) * np.sin(np.pi * y / 2)
    # return np.sin(np.pi * x/2) + np.sin(np.pi * y/2)


if __name__ == '__main__':
    print("Запуск")
    # task3(32, 0.0001)
    task(14, f=f, phi=phi, ksi=ksi, filename='resources/Пример 10', _a=2, _b=2)
    # check_error(14, f=f, phi=phi, ksi=ksi, filename='resources/error', _a=2, _b=2)