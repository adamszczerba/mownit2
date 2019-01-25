import matplotlib.pyplot as plt # do wykresów
import numpy as np              # do macierzy
from scipy import fftpack       # do FFT
import pandas

#1 slow dft

def DFT(x):
    x = np.asarray(x, dtype=float)
    N = x.shape[0]
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j * np.pi * k * n / N)
    return np.dot(M, x)


#2 Cooley-Tukey FFT


def FFT(x):
    x = np.asarray(x, dtype=float)
    N = x.shape[0]

    if N <= 32:
        return DFT(x)
    else:
        X_even = FFT(x[::2])
        X_odd = FFT(x[1::2])
        factor = np.exp(-2j * np.pi * np.arange(N) / N)
        return np.concatenate([X_even + factor[:int(N / 2)] * X_odd,
                               X_even + factor[int(N / 2):] * X_odd])


#3 C-T FFT tests

