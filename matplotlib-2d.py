import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.title('plt x vs y')
plt.xlabel("x")
plt.ylabel("y")
plt.show()
