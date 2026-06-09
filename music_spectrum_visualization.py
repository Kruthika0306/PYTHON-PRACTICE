import numpy as np
import matplotlib.pyplot as plt

signal = np.random.randn(1000)

fft = np.abs(np.fft.fft(signal))

plt.plot(fft[:500])

plt.title("Frequency Spectrum")
plt.show()
