## Convolution
## Convolution_nested  - using for loops

# Setup
from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
from time import time
from skimage import io
import itertools


#%matplotlib inline
plt.rcParams['figure.figsize'] = (10.0, 8.0) # set default size of plots
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['image.cmap'] = 'gray'

def padding(img, kernel):
    w, h = img.shape
    w1, h1 = kernel.shape
    tmp_img = np.zeros((w+2*(w1//2), h+2*(h1//2)))
    tmp_img[w1//2:w1//2+w, h1//2:h1//2+h] = img
    return tmp_img
    
def convolution_nested(img, kernel):
    # img is in the form of np.array
    
    w, h = img.shape
    kernel = np.flip(kernel, axis = 0)
    kernel = np.flip(kernel, axis = 1)
    img = padding(img, kernel)
    output = np.zeros((w, h))
    
    # Iterating through the img
    for i,j in itertools.product(range(0, w),range(0, h)):
        sum = 0
        for x, y in itertools.product(range(0, w1), range(0, h1)):
                sum = sum + img[i+x][j+y]*kernel[x][y]
        output[i][j] = sum
    return output
    
def convolution(img, kernel):
    # img is in the form of np.array
    
    w, h = img.shape
    w1, h1 = kernel.shape
    kernel = np.flip(kernel, axis = 0)
    kernel = np.flip(kernel, axis = 1)
    img = padding(img, kernel)
    output = np.zeros((w, h))
    
    # Iterating through the img
    for i,j in itertools.product(range(0, w),range(0, h)):
        # Iterating through the kernel
        output[i][j] = np.array(img[i:i+w1,j:j+h1]*kernel).sum()
    return output
