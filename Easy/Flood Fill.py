import numpy as np
from skimage.morphology import flood_fill

image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
x = 1
y = 1
color = 2
a = np.array(image)
print(flood_fill(a, (x, y), color))
