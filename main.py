from utils import *
from matplotlib import plot, xlabel, ylabel, title, legend, show
from numpy import linspace

coordinates = generate_x_y(1, 20)

x = linscape(0, coordinates[0], 100)
y = linscape(0, coordinates[1], 100)
plot(x, y, label='linear').show()
xlabel('x label')
ylabel('y label')
title('Simple plot')
# legend()
show()