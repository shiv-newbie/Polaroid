# Setup
from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
from time import time
from skimage import io
from convolution import convolution
from ImageEditting import *
from PIL import Image
import itertools
import sys

plt.rcParams['figure.figsize'] = (10.0, 8.0) # set default size of plots
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['image.cmap'] = 'gray'


def vertical_polaroid(img):
    img = io.imread(img)
    inp_rows, inp_cols, chanels = img.shape
    img_scale = inp_rows/inp_cols

    output_rows = inp_rows+inp_rows//4+inp_rows//8
    output_cols = (int)(output_rows//img_scale)
    col_padding = (output_cols-inp_cols)//2

    output_rows = output_rows+inp_rows//5
    output = np.zeros((output_rows, output_cols, chanels))

    col_fac = 0
    if 2*col_padding != output_cols-inp_cols:
        col_fac = 1

    output[:, :] = 245

    output[inp_rows//8:output_rows-inp_rows//4-inp_rows//5, col_padding:output_cols-col_padding-col_fac] = img
    output1 = output/255
    
#    plt.subplot(1,2,1)
#    plt.imshow(img)
#    plt.title('Original Image')
#    plt.axis('off')
#
#    plt.subplot(1,2,2)
#    plt.imshow(output1)
#    plt.title('Vertical Polaroid')
#    plt.axis('off')
#    plt.show()
    
    return output


def horizontal_polaroid(img):
    img = io.imread(img)
    inp_rows, inp_cols, chanels = img.shape
    img_scale = inp_cols/inp_rows

    output_cols = inp_cols+inp_cols//4+inp_cols//8
    output_rows = (int)(output_cols//img_scale)
    row_padding = (output_rows-inp_rows)//2

    output_cols = output_cols+inp_cols//5
    output = np.zeros((output_rows, output_cols, chanels))

    row_fac = 0
    if 2*row_padding != output_rows-inp_rows:
        row_fac = 1

    output[:, :] = 245

    output[row_padding:output_rows-row_padding-row_fac, inp_cols//8:output_cols-inp_cols//4-inp_cols//5] = img
    output1 = output/255

#    plt.subplot(1,2,1)
#    plt.imshow(img)
#    plt.title('Original Image')
#    plt.axis('off')
#
#    plt.subplot(1,2,2)
#    plt.imshow(output1)
#    plt.title('Horizontal Polaroid')
#    plt.axis('off')
#    plt.show()
    
    return output
    
def fancy_polaroid(img):
    background_blur = blurr(img)
    
    hp = horizontal_polaroid(img)
    h1, w1, channels = hp.shape
    
    blurImgH= resize_image(background_blur, h1+h1//4, w1+w1//6)
    blurImgH[h1//8:h1//8+h1, w1//12:w1//12+w1] = hp
    
    vp = vertical_polaroid(img)
    h1, w1, channels = vp.shape
    
    blurImgV= resize_image(background_blur, h1+h1//6, w1+w1//4)
    blurImgV[h1//12:h1//12+h1, w1//8:w1//8+w1] = vp
    
    plt.subplot(1, 2, 1)
    plt.imshow(blurImgH/255)
    plt.title('Horizontal Fancy Polaroid')
    plt.axis('off')
    
    plt.subplot(1, 2, 2)
    plt.title('Vertical Fancy Polaroid')
    plt.axis('off')
    plt.imshow(blurImgV/255)
    
    plt.show()
    
    return blurImgH/255, blurImgV/255


#if __init__ == __main__:
path = sys.argv[1]
print(path)
h, v = fancy_polaroid(path)
im = Image.fromarray((v * 255).astype(np.uint8))
im.save("PolaroidVertical.jpg")
im = Image.fromarray((h * 255).astype(np.uint8))
im.save("PolaroidHorizontal.jpg")
