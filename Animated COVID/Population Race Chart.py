import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

countries = ["India", "USA", "China", "Brazil"]
values = [1400, 330, 1440, 215]

fig, ax = plt.subplots()

def animate(frame):
    ax.clear()

    updated = [v + frame * 2 for v in values]

    ax.barh(countries, updated)

    ax.set_title(f"Year {2020 + frame}")

ani = FuncAnimation(fig, animate, frames=20)

plt.show()
