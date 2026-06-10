import psutil
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

cpu = []

fig, ax = plt.subplots()

def update(frame):

    cpu.append(psutil.cpu_percent())

    ax.clear()

    ax.plot(cpu)

    ax.set_title("CPU Usage")

ani = FuncAnimation(
    fig,
    update,
    interval=1000
)

plt.show()
