import numpy as np
import math

Var = 4 # Номер варианта
alpha = 0.5 * Var


def func(x, t):
    return alpha * (x ** 2 - 2 * t)


def phi_0(t):
    return 0


def phi_1(t):
    return alpha * t


def psi(t):
    return 0


if __name__ == '__main__':
    a = 1
    T = 0.05
    l = 1
    h = 0.1
    tau = 0.01
    S = tau / h ** 2
    N = int(l / h) + 1
    M = int(T / tau) + 1
    X_i = [i * h for i in range(N)]
    t_j = [j * tau for j in range(M)]
    r_i = len(X_i) # количество узлов по x
    r_j = len(t_j) # количество узлов по t
    U_i_j = np.zeros([r_i, r_j]) # итоговая сетка размером x_i*t_j

    for j in range(M):
        U_i_j[0, j] = phi_0(t_j[j])
        U_i_j[N - 1, j] = phi_1(t_j[j])

    for i in range(N):
        U_i_j[i, 0] = psi(t_j[j])

    a = S
    b = S
    c = (1 - 2 * S)

    for j in range(0, M - 1):
        for i in range(1, N - 1):
            U_i_j[i, j + 1] = a * U_i_j[i - 1, j] + c * U_i_j[i, j] + b * U_i_j[i + 1, j] + \
                              tau * func(X_i[i], t_j[j])

    #const = tau / h**2
    #for i in range(N - 1):
    #    for j in range(M - 1):
    #        U_i_j[i, j+1] = U_i_j[i, j] + const * (U_i_j[i+1, j] - 2 * U_i_j[i, j] + U_i_j[i-1, j]) + \
    #                          tau * func(X_i[i], t_j[j])

    #for i in range(N-1):
    #    for j in range(1, M-1):
    #        U_i_j[i, j+1] = U_i_j[i, j] + T / h**2 * (U_i_j[i+1, j] -
    #                                      2 * U_i_j[i, j] + U_i_j[i-1, j]) + \
    #                                     func(X_i[i], t_j[j])

    for u in U_i_j:
        print('', *map('{:8.4f}'.format, u))