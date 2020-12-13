import numpy as np
import time
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation


#############################
#                           #
#     Тестовый пример       #
#                           #
#############################


def phi(x, y):
    return np.sin(np.pi * x / 2) * np.sin(np.pi * y)


def ff(x, y, t):
    return np.sin(np.pi * x / 2) * np.sin(np.pi * y) * np.cos(2 * t) * (4 - np.pi ** 2 * 5 / 4)


def lambd(n, m):
    return np.pi ** 2 * (n * n + m * m) / 4


def v(x, y, n, m):
    return np.sin(n * np.pi * x / 2) * np.sin(m * np.pi * y / 2)


def B(n, m):
    if n == 1 or m == 2:
        return 0
    return -8 * np.sin(np.pi * n / 2) * np.cos(np.pi * m / 2) / ((np.pi ** 2) * (m * m - 4) * (n * n - 1))


def B2(n, m):
    return 0


def u_elementary(x, y, t, n, m):
    return (B(n, m) * np.cos(lambd(n, m) ** (0.5) * t) + B2(n, m) * np.sin(lambd(n, m) ** (0.5) * t)) * v(x, y, n, m)


def my_u(x, y, t):
    return phi(x, y) * np.cos(np.sqrt(lambd(1, 2)) * t)


def u(x, y, t, M=100, N=100):
    #    if (x == 0 or y == 0 or x == 5 or y == 5):
    #        return 0
    res = 0
    for m in range(1, M + 1):
        for n in range(1, N + 1):
            res += u_elementary(x, y, t, n, m)
    return res


def update_plot(frame_number, zarray, plot):
    plot[0].remove()
    plot[0] = ax.plot_surface(x, y, zarray[:, :, frame_number], cmap="magma")


time0 = time.time()
N = 250  # Meshsize
fps = 10  # frame per sec
frn = 62  # frame number of the animation

x = np.linspace(0, 2, N + 1, endpoint=True)
x, y = np.meshgrid(x, x)
zarray = np.zeros((N + 1, N + 1, frn))

for i in range(frn):
    zarray[:, :, i] = my_u(x, y, 0.1 * i)
box_1 = {'facecolor': 'white',  # цвет области
         'edgecolor': 'black',  # цвет крайней линии
         'boxstyle': 'round'}

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.text(0, 0, 11, s='t = [0, 6)')

plot = [ax.plot_surface(x, y, zarray[:, :, 0], color='0.75', rstride=1, cstride=1)]
ax.set_zlim(0, 2)
ani = FuncAnimation(fig, update_plot, frn, fargs=(zarray, plot), interval=1000 / fps)
print(time.time() - time0)
fn = 'resources/myplotTest'
ani.save(fn + '.mp4', writer='ffmpeg', fps=fps)
ani.save(fn + '.gif', writer='imagemagick', fps=fps)
