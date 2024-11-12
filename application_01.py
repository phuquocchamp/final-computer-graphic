import numpy as np
import matplotlib.pyplot as plt

def basic_noise(width, height, seed=None, contrast=1.0):
    if seed:
        np.random.seed(seed)
    noise = np.random.rand(width, height) * contrast
    return noise

# Parameters
width, height = 200, 200
seed = 42
contrast = 1.5

# Generate and visualize
noise = basic_noise(width, height, seed=seed, contrast=contrast)
plt.imshow(noise, cmap='gray')
plt.colorbar()
plt.title("Random Noise Background")
plt.show()
