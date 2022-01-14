import numpy as np
from random import random
from math import floor, sin


def generate_perlin_noise_2d(shape, res=(1, 1)):
    def f(t):
        return 6*t**5 - 15*t**4 + 10*t**3

    shape, res = np.array(shape), np.array(res)
    delta = res / shape
    d = shape // res
    grid = np.mgrid[0:res[0]:delta[0], 0:res[1]:delta[1]].transpose(1, 2, 0) % 1
    # Gradients
    angles = 2*np.pi*np.random.rand(res[0]+1, res[1]+1)
    gradients = np.dstack((np.cos(angles), np.sin(angles)))
    g00 = gradients[0:-1, 0:-1].repeat(d[0], 0).repeat(d[1], 1)
    g10 = gradients[1:, 0:-1].repeat(d[0], 0).repeat(d[1], 1)
    g01 = gradients[0:-1, 1:].repeat(d[0], 0).repeat(d[1], 1)
    g11 = gradients[1:, 1:].repeat(d[0], 0).repeat(d[1], 1)
    # Ramps
    n00 = np.sum(grid * g00, 2)
    n10 = np.sum(np.dstack((grid[:, :, 0]-1, grid[:, :, 1])) * g10, 2)
    n01 = np.sum(np.dstack((grid[:, :, 0], grid[:, :, 1]-1)) * g01, 2)
    n11 = np.sum(np.dstack((grid[:, :, 0]-1, grid[:, :, 1]-1)) * g11, 2)
    # Interpolation
    t = f(grid)
    n0 = n00*(1-t[:, :, 0]) + t[:, :, 0]*n10
    n1 = n01*(1-t[:, :, 0]) + t[:, :, 0]*n11
    return np.sqrt(2)*((1-t[:, :, 1])*n0 + t[:, :, 1]*n1)


def perlin(distance, resolution):
    return generate_perlin_noise_2d((resolution*distance, resolution*distance), (distance, distance))


def worley(size, points=10): ...


def D(A, B):
    M = A.shape[0]
    N = B.shape[0]

    A_dots = (A*A).sum(axis=1).reshape((M, 1))*np.ones(shape=(1, N))
    B_dots = (B*B).sum(axis=1)*np.ones(shape=(M, 1))
    D_squared = A_dots + B_dots - 2*A.dot(B.T)

    zero_mask = np.less(D_squared, 0.0)
    D_squared[zero_mask] = 0.0
    return np.sqrt(D_squared)


arr = np.array([[0, 0], [1, 1], [2, 5]])
arr2 = np.array([[0, 0], [1, 1], [5, 5]])
print(D(arr, arr2))
