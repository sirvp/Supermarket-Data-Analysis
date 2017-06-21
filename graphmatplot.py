import numpy as np
csv=np.genfromtxt('ans.csv',delimiter=",", dtype=None)

import matplotlib.pyplot as plt
plt.plot(csv)
plt.xlabel('Day')
plt.ylabel('Profit')
plt.show()

