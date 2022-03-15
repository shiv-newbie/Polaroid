# Setup
import numpy as np
from skimage import io


def gaussian_filter(sigma):
    # Generate 1D kernel
    
    ks_half = int(np.ceil(3 * sigma)) # half kernel size
    x = np.linspace(-ks_half, ks_half, 2*ks_half + 1, dtype=float) # len(x) = 2*ks_half + 1
    kernel = gauss(x, sigma)
    kernel = kernel / np.sum(kernel) # make sure the sum of weights in kernel = 1

    return kernel

def gauss(x, sigma):
    return 1 / (np.sqrt(2 * np.pi) * sigma) * np.exp(-x**2 / (2 * sigma**2))
