#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def to_grayscale(img):
    r, g, b, = img[:,:,0], img[:,:,1], img[:,:,2]
    return 0.2126 * r + 0.7152 *g + 0.0722 * b

def to_red(img):
    img[:,:,1] = img[:,:,2] = 0
    return img

def to_green(img):
    img[:,:,0] = img[:,:,2] = 0
    return img

def to_blue(img):
    img[:,:,0] = img[:,:,1] = 0
    return img

def main():
    image = plt.imread('src\painting.png')
    gray = to_grayscale(image.copy())
    plt.imshow(gray, cmap='gray')

    fig, ax = plt.subplots(3,1)
    ax[0].imshow(to_red(image.copy()))
    ax[1].imshow(to_green(image.copy()))
    ax[2].imshow(to_blue(image.copy()))
    plt.show()

if __name__ == "__main__":
    main()
