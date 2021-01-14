import matplotlib.pyplot as plt
import numpy as np
import math

points = 50
stop = 2*math.pi
step =  stop / points
xpoints = np.arange(0,stop,step)

fig, (ax1, ax2) = plt.subplots(2)
fig.suptitle('Vertically stacked subplots')
ax1.set_ylabel("sin")
ax1.plot(xpoints, np.sin(xpoints))
ax2.set_ylabel("cos")
ax2.plot(xpoints, np.cos(xpoints))
plt.show()
