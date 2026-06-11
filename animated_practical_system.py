import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

n = 100

x = np.random.rand(n)
y = np.random.rand(n)

vx = np.random.randn(n) * 0.01
vy = np.random.randn(n) * 0.01

fig, ax = plt.subplots()
scatter = ax.scatter(x, y)

def update(frame):
    global x, y

    x += vx
    y += vy

    scatter.set_offsets(np.c_[x, y])
    return scatter,

ani = FuncAnimation(fig, update, interval=30)
plt.show()
