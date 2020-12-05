import numpy as np
import time
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation


#############################
#                           #
#       Случай (x+y)        #
#                           #
#############################


def phi(x, y):
    return x + y


def lambd(n, m):
    return np.pi ** 2 * (n * n + m * m) / 25


def v(x, y, n, m):
    return 2 / 5 * np.sin(n * np.pi * x / 5) * np.sin(m * np.pi * y / 5)


def B(n, m):
    return 50 / (np.pi ** 2 * m * n) * ((-1) ** m * (-1) ** n * 2 + (-1) ** (n + 1) + (-1) ** (m + 1))


def nullTozhd(n, m):
    return 0


def B2(n, m):
    return lambd(n, m) ** (-0.5) * B(n, m)


def u_elementary(x, y, t, n, m):
    return (nullTozhd(n, m) * np.cos(lambd(n, m) ** (0.5) * t) + B2(n, m) * np.sin(lambd(n, m) ** (0.5) * t)) * v(x, y, n, m)


def u(x, y, t, M=100, N=100):
    #    if (x == 0 or y == 0 or x == 5 or y == 5):
    #        return 0
    res = 0
    for m in range(1, M + 1):
        for n in range(1, N + 1):
            res += u_elementary(x, y, t, n, m)
    return res


time0 = time.time()
N = 150  # Meshsize
fps = 10  # frame per sec
frn = 50  # frame number of the animation

x = np.linspace(0, 5, N + 1, endpoint=True)
x, y = np.meshgrid(x, x)
zarray = np.zeros((N + 1, N + 1, frn))

for i in range(frn):
    zarray[:, :, i] = u(x, y, 0.1 * i, 32, 32)
box_1 = {'facecolor': 'white',  # цвет области
         'edgecolor': 'black',  # цвет крайней линии
         'boxstyle': 'round'}


def update_plot(frame_number, zarray, plot):
    plot[0].remove()
    plot[0] = ax.plot_surface(x, y, zarray[:, :, frame_number], cmap="magma")



fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.text(0, 0, 11, s='t = [0, 5)')

plot = [ax.plot_surface(x, y, zarray[:, :, 0], color='0.75', rstride=1, cstride=1)]
ax.set_zlim(-5, 10)
ani = FuncAnimation(fig, update_plot, frn, fargs=(zarray, plot), interval=1000 / fps)
print(time.time() - time0)
fn = 'resource/myplot'
ani.save(fn + '.mp4', writer='ffmpeg', fps=fps)
ani.save(fn + '.gif', writer='imagemagick', fps=fps)
