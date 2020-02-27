'''
  File name: getCoefficientMatrix.py
  Author: Luoli Wang
  Date created: Sep 25,2019
'''
import numpy as np


def getCoefficientMatrix(indexes):
    N = np.amax(indexes)
    coeffA = np.zeros([N, N])
    for index in range(1, N + 1):
        i, j = np.where(indexes == index)
        index -= 1
        coeffA[index, index] = 4
        if indexes[i + 1, j] > 0: coeffA[index, indexes[i + 1, j]-1] = -1
        if indexes[i - 1, j] > 0: coeffA[index, indexes[i - 1, j]-1] = -1
        if indexes[i, j + 1] > 0: coeffA[index, indexes[i, j + 1]-1] = -1
        if indexes[i, j - 1] > 0: coeffA[index, indexes[i, j - 1]-1] = -1

    return coeffA
