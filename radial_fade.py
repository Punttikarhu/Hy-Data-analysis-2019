#!/usr/bin/env python3
import math
import numpy as np
import matplotlib.pyplot as plt


def center(a):
    center_y, center_x = (a.shape[0]-1)/2, (a.shape[1]-1)/2
    print(center_y, center_x)
    return (center_y, center_x)   # note the order: (center_y, center_x)

def radial_distance(a):
    height, width = a.shape[0], a.shape[1]
    center_y, center_x = center(a)
    b = np.zeros((height, width))
    for i in range(height):
        for j in range(width):
            b[i,j] = ((i-center_y)**2+(j-center_x)**2)**0.5
    print(f'b = {b}')
    return b

def scale(a, tmin=0.0, tmax=1.0):
    """Returns a copy of array 'a' with its values scaled to be in the range
[tmin,tmax]."""
    b = a.copy()
    norm = b - np.min(b)
    if np.max(norm) != 0:
        scaled = norm/np.max(norm)
    else:
        scaled = norm
    print(f'scaled = {scaled}')
    return scaled

def radial_mask(a):
    b = 1 - scale(radial_distance(a))
    print(f'b = {b}')
    return b

def radial_fade(a):
    mask = radial_mask(a)
    mask = np.reshape(mask, (mask.shape[0],mask.shape[1], 1))
    a *= mask
    print(a)
    return a

def main():
    #img = plt.imread('painting.png')
    #img = np.random.randint(1, 10, (3,3, 3))
    n = 1
    img = np.zeros((n, n, 3))
    print(img)
    fig, ax = plt.subplots(3, 1)
    ax[0].imshow(img)
    ax[1].imshow(radial_mask(img))
    ax[2].imshow(radial_fade(img))
    plt.show()

if __name__ == "__main__":
    main()
