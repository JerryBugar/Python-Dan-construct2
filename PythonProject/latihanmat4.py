import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([1,2,3,4,5])
y1 = np.array([3,7,2,8,5])
x2 = np.array([1,2,3,4,5])
y2 = np.array([8,1,3,6,2])

plt.plot(x1,y1,x2,y2)
plt.show()