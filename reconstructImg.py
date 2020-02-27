'''
  File name: reconstructImg.py
  Author: Luoli Wang
  Date created: Sep 25,2019
'''
import numpy as np
import cv2


def reconstructImg(indexes, red, green, blue, targetImg):
    b, g, r = cv2.split(targetImg)
    N = np.amax(indexes)
    for index in range(1, N + 1):
        i, j = np.where(indexes == index)
        r[i, j] = red[index - 1]
        b[i, j] = blue[index - 1]
        g[i, j] = green[index - 1]

    resultImg = cv2.merge((b, g, r))

    return resultImg
