import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1,2,3,4,5])
ypoints = np.array([3,7,2,8,5])

plt.plot(xpoints, ypoints, marker='o', ms=10, mfc='#ff3300')

plt.plot(xpoints, ypoints, marker='d', ms=10, mec='b')

plt.plot(xpoints, ypoints, marker='d', ms=10, mfc='w')

plt.plot(xpoints, ypoints, linestyle='dashed', color='b')

plt.plot(xpoints, ypoints, ls='--', color='g')  


plt.plot(xpoints, ypoints, color='m')

plt.plot(xpoints, ypoints, ls=':', c='r')

plt.show()