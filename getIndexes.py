'''
  File name: getIndexes.py
  Author: Luoli Wang
  Date created: Sep 25,2019
'''
import numpy as np


def getIndexes(mask, targetH, targetW, offsetX, offsetY):
    srcH, srcW = mask.shape
    indexes = np.zeros([targetH, targetW], dtype=int)
    cnt = 0
    for i in range(0, srcH):
        for j in range(0, srcW):
            if mask[i, j] == 255:
                cnt += 1
                indexes[i + offsetX, j + offsetY] = cnt
            else:
                indexes[i + offsetX, j + offsetY] = 0
    return indexes



