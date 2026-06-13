import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x = np.linspace(0,10,500)

fig, ax = plt.subplots()

line, = ax.plot([],[])

def update(frame):

    y = np.sin(x*3 + frame/5)

    line.set_data(x,y)

    return line,

ax.set_xlim(0,10)
ax.set_ylim(-2,2)

ani = FuncAnimation(fig,update)

plt.show()
