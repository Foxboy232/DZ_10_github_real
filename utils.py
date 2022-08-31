import random


def generate_x_y(a, b):
    if a < b:
        a, b = b, a
    x_y_list = []
    for _ in range(2):
        x_y_list.append(random.randint(a, b))
    return x_y_list[0], x_y_list[1]
