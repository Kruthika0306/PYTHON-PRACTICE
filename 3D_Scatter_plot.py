import plotly.express as px
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "x": np.random.rand(100),
    "y": np.random.rand(100),
    "z": np.random.rand(100),
    "size": np.random.randint(5, 20, 100)
})

fig = px.scatter_3d(
    df,
    x="x",
    y="y",
    z="z",
    size="size"
)

fig.show()
