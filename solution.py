import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

ht = 0.1
hx = 0.1
hy = 0.1
a = 2
b = 2


# n - x/y   m - t
def create_scheme(n, m, phi, ksi, func):
    C1 = hx**2 * hy**2
    C2 = ht**2 * hy**2
    C3 = ht**2 * hx**2
    C4 = 2*ht**2 * hx**2 * hy**2
    C0 = -2*(C1 + C2 + C3)
    _n = n+1
    size_quad = _n * _n
    _A = np.zeros((size_quad * m, size_quad * m))
    _b = np.zeros(size_quad * m)
    _x = np.zeros(size_quad * m)
    # начальные условия
    for i in range(1, _n - 1):
        for j in range(1, _n - 1):
            tmp = i * _n + j
            _x[tmp] = phi(j * hx, i * hy)
            _x[tmp + size_quad] = ht * ksi(j * hx, i * hy) + _x[tmp]
    for k in range(2, m-1):
        for i in range(1, _n-1):
            for j in range(1, _n-1):
                tmp = k * size_quad + i * _n + j
                _A[tmp][tmp] = C0
                _A[tmp][tmp - size_quad] = C1
                _A[tmp][tmp + size_quad] = C1
                _A[tmp][tmp + _n] = C2
                _A[tmp][tmp - _n] = C2
                _A[tmp][tmp - 1] = C3
                _A[tmp][tmp + 1] = C3
                _b[tmp] = C4 * func(j*hx, i*hy, k*ht)
    k = (m-1)
    for i in range(1, _n - 1):
        for j in range(1, _n - 1):
            tmp = k * size_quad + i * _n + j
            _A[tmp][tmp] = C0
            _A[tmp][tmp - size_quad] = C1
            _A[tmp][tmp + _n] = C2
            _A[tmp][tmp - _n] = C2
            _A[tmp][tmp - 1] = C3
            _A[tmp][tmp + 1] = C3
            _b[tmp] = C4 * func(j * hx, i * hy, k * ht)
    return _A, _b, _x


def r_fun(A, b, x):
    return b - A.dot(x)


def tau_fun(A, b, x):
    r = r_fun(A, b, x)
    return np.vdot(r, r) / np.vdot(A.dot(r), r)


def steepest_descent(A, b, x0, eps):
    step = 0
    x_old = x0
    r = r_fun(A, b, x_old)
    r0_norm = np.linalg.norm(r, 1)
    t = tau_fun(A, b, x_old)
    x_new = x_old + t * r
    while (np.linalg.norm(r, 1) / r0_norm > eps):
        x_old = x_new
        r = r_fun(A, b, x_old)
        t = tau_fun(A, b, x_old)
        x_new = x_old + t * r
        step += 1
    print('step =', step)
    return x_new


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
        plot[0] = ax.plot_surface(x, y, zarray[frame_number, :, :], cmap="magma")

    x = np.linspace(0, a, n + 1, endpoint=True)
    y = np.linspace(0, b, n + 1, endpoint=True)
    x, y = np.meshgrid(x, y)
    global hx, hy, ht
    hx = a / n
    hy = b / n
    ht = 0.1
    m = frn
    A, vec_b, x0 = create_scheme(n, m, phi, ksi, f)
    print('log = create_sсheme')

    zarray = np.reshape(steepest_descent(A, vec_b, x0, 0.0001), newshape=(m, n+1, n+1))
    print('log =  solve')
    box_1 = {'facecolor': 'white',  # цвет области
             'edgecolor': 'black',  # цвет крайней линии
             'boxstyle': 'round'}

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.text(0, 0, 11, s='t = [0, 6)')

    plot = [ax.plot_surface(x, y, zarray[0, :, :], color='0.75', rstride=1, cstride=1)]
    ax.set_zlim(0, 2)
    print('log = create animation')
    ani = FuncAnimation(fig, update_plot, frn, fargs=(zarray, plot), interval=1000 / fps)
    ani.save(filename + '.mp4', writer='ffmpeg', fps=fps)
    print('log = mp4 ready')
    ani.save(filename + '.gif', writer='imagemagick', fps=fps)
    print('log = gif ready')
