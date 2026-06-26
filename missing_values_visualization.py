import pandas as pd
import missingno as msno
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

msno.matrix(df)

plt.show()
