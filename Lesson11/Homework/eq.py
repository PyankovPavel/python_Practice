import numpy as np
import matplotlib.pyplot as plt


def func(x):
    eq = -12 * x ** 4 * np.sin(np.cos(x)) - 18 * x ** 3 + 5 * x * 2 + 10 * x - 30
    return eq


def roots(x1, x2):
    count = 0
    y = func(x1)
    for i in np.arange(x1, x2, 0.001):
        if y * func(i) < 0:
            count += 1
        y = func(i)
    return count


def drawing(x, legenda):
    plt.figure(figsize=(10, 10))
    plt.xlabel('Ось_X')
    plt.ylabel('Ось_Y')
    plt.grid()
    plt.plot(x, func(x))
    plt.title(legenda, fontsize=16)
    plt.show()


text = f'Общий график функции, корней в нем {roots(-100, 100)} '
x = np.arange(-100, 100, 0.01)
drawing(x, text)
text = f'График на промежутке от -10 до 10, корней в нем {roots(-5, 5)}'
x = np.arange(-5, 5, 0.01)
drawing(x, text)
