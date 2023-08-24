import numpy as np
from skimage.metrics import structural_similarity
from skimage.metrics import mean_squared_error
from skimage.metrics import peak_signal_noise_ratio
from sklearn.metrics import mean_absolute_error
from scipy.stats import pearsonr

a = np.array([[1, 1, 1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1, 1, 1],
              [3, 3, 3, 3, 3, 3, 3],
              [3, 3, 3, 3, 3, 3, 3],
              [0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0]], dtype=np.float32)

b = np.array([[1, 1, 1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1, 1, 1],
              [3, 3, 2, 2, 3, 2, 3],
              [3, 3, 3, 3, 3, 3, 3],
              [3, 3, 3, 3, 3, 3, 3],
              [0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0]], dtype=np.float32)

c = np.array([[0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0],
              [1, 1, 1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1, 1, 1],
              [0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0]])

# a = a[a != 0]
a = a[np.any(c != 0, axis=1)]
b = b[np.any(c != 0, axis=1)]

print(a)
print("\n")
print(b)

print(structural_similarity(a, b, win_size=None, data_range=float))
