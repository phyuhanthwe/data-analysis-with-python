#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from skimage import io

def to_grayscale(img):
    # img = plt.imread(image_path)
    red, green, blue = 0.2126, 0.7152, 0.0722
    gray_img = (img[:, :, 0]*red +
                img[:, :, 1]*green +
                img[:, :, 2]*blue
                )
    return gray_img

def to_red(img):
    # img = plt.imread(image_path)
    red_img = np.copy(img)
    red_img[:, :, 1] = 0
    red_img[:, :, 2] = 0
    return red_img

def to_green(img):
    # img = plt.imread(image_path)
    green_img = np.copy(img)
    green_img[:, :, 0] = 0
    green_img[:, :, 2] = 0
    return green_img

def to_blue(img):
    # img = plt.imread(image_path)
    blue_img = np.copy(img)
    blue_img[:, :, 0] = 0
    blue_img[:, :, 1] = 0
    return blue_img


def main():
    image_path = 'src/painting.png'
    image = io.imread(image_path)
    gray_img = to_grayscale(image)
    # plt.gray()
    plt.imshow(gray_img, cmap="gray")
    plt.show()

    red_img =  to_red(image)
    green_img =  to_green(image)
    blue_img =  to_blue(image)
    fig, ax = plt.subplots(3, 1)
    ax[0].imshow(red_img)
    ax[1].imshow(green_img)
    ax[2].imshow(blue_img)
    plt.show()
    pass

if __name__ == "__main__":
    main()
