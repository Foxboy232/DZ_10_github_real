from matplotlib import linscape
import random


def generate_x_y(a, b):
    if a < b:
        a, b = b, a
    x_y_list = []
    for _ in range(2):
        random.randint(a, b)
    _ = linscape(0, 2, 10)
    return x_y_list[0], x_y_list[1]
