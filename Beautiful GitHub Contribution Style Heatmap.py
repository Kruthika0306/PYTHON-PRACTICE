# github_style_heatmap.py

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = np.random.randint(0, 10, size=(7, 52))

plt.figure(figsize=(15, 4))

sns.heatmap(
    data,
    cmap="Greens",
    linewidths=0.5,
    linecolor='gray'
)

plt.title("Yearly Productivity Heatmap")
plt.show()
