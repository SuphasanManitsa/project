import numpy as np
a = np.array([1,2,3])
b = np.array([4,5,6])
p = np.poly1d(np.polyfit(a, b, 1))
print(np.roots(p))