#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from skimage import io

def center(a):
    h, w = a.shape[:2]
    center_x = (w-1 )/ 2
    center_y = (h-1) / 2
    return (center_y,center_x)   # note the order: (center_y, center_x)

def radial_distance(a):
    h, w = a.shape[:2]
    center_y, center_x = (h-1) / 2, (w-1) / 2
    y_indices, x_indices = np.meshgrid(np.arange(h), np.arange(w), indexing="ij")
    distance = np.sqrt((y_indices - center_y)**2 + (x_indices - center_x)**2)
    return distance

def scale(a, tmin=0.0, tmax=1.0):
    """Returns a copy of array 'a' with its values scaled to be in the range
[tmin,tmax]."""
    amin = np.min(a)
    amax = np.max(a)
    scale_a = tmin + (((a - amin) * (tmax - tmin)) / (amax - amin))
    return  scale_a

def radial_mask(a):
    distance = radial_distance(a)
    scale_distance = scale(distance)
    return 1 - scale_distance

def radial_fade(a):
    mask = radial_mask(a)
    if a.ndim == 3: 
        mask = mask[..., np.newaxis] 
    return a * mask

def main():
    image_path = 'src/painting.png'
    image = io.imread(image_path)
    # print(center(np.zeros((10, 11, 3))))
    # print(radial_distance(image))
    mask = radial_mask(image)
    faded_image = radial_fade(image)
    fig, axes = plt.subplots(3, 1)
    axes[0].imshow(image)
    axes[1].imshow(mask, cmap='gray')
    axes[2].imshow(faded_image)
    plt.show()
    pass

if __name__ == "__main__":
    main()
