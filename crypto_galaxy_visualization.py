# crypto_galaxy.py

import matplotlib.pyplot as plt
import numpy as np
import random

coins = [
    ("Bitcoin", 1000),
    ("Ethereum", 700),
    ("Solana", 400),
    ("Dogecoin", 300),
    ("Cardano", 350),
]

fig, ax = plt.subplots(figsize=(10, 10))
ax.set_facecolor("black")

for coin, size in coins:
    x = random.uniform(-10, 10)
    y = random.uniform(-10, 10)

    circle = plt.Circle((x, y), size / 200, alpha=0.7)
    ax.add_patch(circle)

    ax.text(x, y, coin, color="white", ha="center")

ax.set_xlim(-12, 12)
ax.set_ylim(-12, 12)

plt.title("Crypto Galaxy Map", color="white", fontsize=20)
plt.show()
