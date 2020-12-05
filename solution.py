import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

ht = 0.1
hx = 0.1
hy = 0.1
a = 4
b = 4


#########################
#                       #
# Вероятно неправильный #
#      явный метод      #
#                       #
#########################


def scheme(u0, u1, f, t):
    u2 = 2 * u1 - u0
    for i in range(1, u2.shape[0]-1):
        for j in range(1, u2.shape[1]-1):
            u2[i][j] += ht ** 2 * ((u1[i + 1][j] - 2 * u1[i][j] + u1[i - 1][j]) / hx ** 2 + (
                        u1[i][j + 1] - 2 * u1[i][j] + u1[i][j - 1]) / hy ** 2 + f(i * hx, j * hy, t))
    return u2


def show_plot(u_numeric):
    fig = plt.figure()
    ax = fig.add_subplot(121, projection='3d')
    x, y = np.meshgrid(np.linspace(0, a, u_numeric.shape[0], endpoint=True),
                       np.linspace(0, b, u_numeric.shape[1], endpoint=True))
    ax.plot_surface(x, y, u_numeric, cmap='inferno', rstride=1, cstride=1)
    ax = fig.add_subplot(122)
    ax.axis('off')
    ax.imshow(u_numeric, cmap='inferno')
    plt.show()
    return 0


def task(n, f, phi, ksi, filename):
    fps = 10  # frame per sec
    frn = 62  # frame number of the animation

    def update_plot(frame_number, zarray, plot):
        plot[0].remove()
        plot[0] = ax.plot_surface(x, y, zarray[:, :, frame_number], cmap="magma")

    x = np.linspace(0, 2, n + 1, endpoint=True)
    x, y = np.meshgrid(x, x)
    global hx, hy, ht
    hx = a / n
    hy = b / n
    ht = 0.1
    u0 = np.zeros((n + 1, n + 1))
    u1 = np.zeros((n + 1, n + 1))
    for i in range(1, n):
        for j in range(1, n):
            u0[i][j] = phi(i * hx, j * hy)
            u1[i][j] = 2 * ht * ksi(i * hx, j * hy) + u0[i][j]
    t = 0.1

    zarray = np.zeros((n + 1, n + 1, frn))

    for i in range(frn):
        t += ht
        u2 = scheme(u0, u1, f, t)
        zarray[:, :, i] = u2
        u0 = u1
        u1 = u2

    box_1 = {'facecolor': 'white',  # цвет области
             'edgecolor': 'black',  # цвет крайней линии
             'boxstyle': 'round'}

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.text(0, 0, 11, s='t = [0, 6)')

    plot = [ax.plot_surface(x, y, zarray[:, :, 0], color='0.75', rstride=1, cstride=1)]
    ax.set_zlim(0, 2)
    ani = FuncAnimation(fig, update_plot, frn, fargs=(zarray, plot), interval=1000 / fps)
    ani.save(filename + '.mp4', writer='ffmpeg', fps=fps)
    ani.save(filename + '.gif', writer='imagemagick', fps=fps)
