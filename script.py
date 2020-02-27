import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from seamlessCloningPoisson import seamlessCloningPoisson

if __name__ == "__main__":

    sourceImg = np.array(Image.open('1_source.jpg').convert('RGB'))
    targetImg = np.array(Image.open('1_background.jpg').convert('RGB'))
    # mask = main('1_source.jpg')
    mask = np.array(Image.open('1_mask.png').convert('L'))

    height, width, channel = np.array(targetImg).shape
    offsetX = 200
    offsetY = 250
    E = seamlessCloningPoisson(sourceImg, targetImg, mask, offsetX, offsetY)

    plt.imshow(E)
    plt.axis('on')
    plt.show()
