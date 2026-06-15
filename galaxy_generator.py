import numpy as np
import matplotlib.pyplot as plt

n = 5000

theta = np.random.rand(n) * 10*np.pi

r = theta + np.random.randn(n)

x = r*np.cos(theta)
y = r*np.sin(theta)

plt.figure(figsize=(8,8))
plt.scatter(x,y,s=0.5)

plt.axis('equal')
plt.show()
