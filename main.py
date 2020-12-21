import numpy as np
from solution import task, check_error


def f(x, y, t):
    return np.sin(np.pi * x / 2) * np.sin(np.pi * y) * np.cos(2 * t) * (-4 + 5 / 4 * np.pi ** 2)
    # return 0
    # return np.sin(np.pi * x / 2) * np.sin(np.pi * y) * np.cos(2 * t)
    # return np.sin(np.pi * x / 2) * np.sin(np.pi * y / 2) * np.exp(0.3*t)
    # return (np.sin(np.pi * x / 2) + np.sin(np.pi * y)) * np.cos(2 * t)
    # return 0.2*(np.exp(x) + np.exp(y))*np.sin(t)

    # return np.sin(np.pi * x / 2) * np.sin(np.pi * y) * np.cos(t)
    # return 5*np.sin(np.pi * x / 2) * np.sin(2 * np.pi * y) * np.cos(2 * t)
    # return np.exp(x*y)*np.sin(np.pi * x / 2) * np.sin(np.pi * y) * np.cos(2 * t)
    # return (np.sin(np.pi * x / 2) + np.sin(np.pi * y)) * np.cos(2 * t)


def phi(x, y):
    return np.sin(np.pi * x / 2) * np.sin(np.pi * y)
    # return 0
    # return np.sin(np.pi * x / 2) * np.sin(np.pi * y)

def ksi(x, y):
    return 0
    # return np.sin(np.pi * x / 2) * np.sin(np.pi * y / 2)
    # return np.sin(np.pi * x/2) + np.sin(np.pi * y/2)


if __name__ == '__main__':
    print("Запуск")
    # task(14, _ht=0.04, f=f, phi=phi, ksi=ksi, filename='resources/Пример 5', _a=2, _b=2)
    check_error(8, _ht=0.1, f=f, phi=phi, ksi=ksi, filename='resources/_error0', _a=2, _b=2)