import numpy as np
import bitstring as bs
from matplotlib import pyplot as plt


#zadanie1
def zadanie1():
    x = np.float32(1/3)
    y = np.float64(1/3)
    z = np.float32(1/3)
    w = np.float64(z)

    print(x)
    print(y)
    print(w)

    print(bs.BitArray(float=x, length=32).bin)
    print(bs.BitArray(float=y, length=64).bin)
    print(bs.BitArray(float=z, length=64).bin)

zadanie1()


#zadanie2
def zadanie2():
    lst = []
    for i in np.linspace(1.0, 1000.0, 1000):
        lst.append(np.spacing(i))
    plt.plot(lst)
    plt.show()

zadanie2()


#zadanie4
def unstable_alg(x, y):
    return np.float64(x**2 - y**2)


#istnieje gorne ograniczenie na blad wzgledny
def stable_alg(x, y):
    return np.float64((x+y)*(x-y))

def test():
    x = 0.0001
    y = 0.0002

    for i in range(10000):
        a = unstable_alg(x, y)
        b = stable_alg(x, y)
        print(a)
        print(b)
        print(abs(a-b))
        print()

        x+=1
        y+=1

test()



