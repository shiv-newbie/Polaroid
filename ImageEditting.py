# Setup
from __future__ import print_function
from gaussianFilter import gaussian_filter
from convolution import convolution
import numpy as np
import matplotlib.pyplot as plt
from time import time
from skimage import io
import itertools

def blurr(img):
    
    img = io.imread(img)
    inp_rows, inp_cols, chanels = img.shape
    img_scale = inp_rows/inp_cols
    
    kernel = gaussian_filter(8)
    kernel = np.reshape(kernel, (7, 7))
    
    w1, h1 = kernel.shape

    output = np.zeros((img.shape))
    o = np.zeros((img.shape))
   
    output[:, :, 0] = convolution(img[:,:,0], kernel)
#    o[:, :, 0] = output[: , :, 0]/255
    output[:, :, 1] = convolution(img[:,:,1], kernel)
#    o[:, :, 1] = output[: , :, 1]/255
    output[:, :, 2] = convolution(img[:,:,2], kernel)
#    o[:, :, 2] = output[: , :, 2]/255
    
#    plt.subplot(1, 2, 1)
#    plt.imshow(img)
#    plt.title('Original Image')
#    plt.axis('off')
#
#    plt.subplot(1, 2, 2)
#    plt.title('Blurr')
#    plt.axis('off')
#    plt.imshow(o)

    plt.show()
    
    return output
    
def resize_image(input_image, output_rows, output_cols):

    input_rows, input_cols, channels = input_image.shape
    output_image = np.zeros(shape=(output_rows, output_cols, 3))
   
    row_scale_factor = (input_rows/output_rows)
    col_scale_factor = (input_cols/output_cols)

    for i,j in itertools.product(range(0, output_rows), range(0, output_cols)):
        output_image[i][j] = input_image[int(i*row_scale_factor)][int(j*col_scale_factor)]
        
    return output_image
