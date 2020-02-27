'''
  File name: seamlessCloningPoisson.py
  Author:
  Date created:
'''
import numpy as np
from getIndexes import getIndexes
from getCoefficientMatrix import getCoefficientMatrix
from getSolutionVect import getSolutionVect
from reconstructImg import reconstructImg
from scipy.sparse import linalg as linalg
import cv2


def seamlessCloningPoisson(sourceImg, targetImg, mask, offsetX, offsetY):
    source_blue, source_green, source_red = np.array(cv2.split(sourceImg))
    target_blue, target_green, target_red = np.array(cv2.split(targetImg))

    targetH, targetW = target_red.shape
    indexes = getIndexes(mask, targetH, targetW, offsetX, offsetY)
    A = getCoefficientMatrix(indexes)
    print('got A')

    b_red = getSolutionVect(indexes, source_red, target_red, offsetX, offsetY)
    b_blue = getSolutionVect(indexes, source_blue, target_blue, offsetX, offsetY)
    b_green = getSolutionVect(indexes, source_green, target_green, offsetX, offsetY)
    print('got b')

    x_red = np.array(linalg.spsolve(A, b_red))
    print('x_red_finished')
    x_green = np.array(linalg.spsolve(A, b_green))
    print('x_green_finished')
    x_blue = np.array(linalg.spsolve(A, b_blue))
    print('x_blue_finished')

    x_red = np.clip(x_red, 0, 255)
    x_green = np.clip(x_green, 0, 255)
    x_blue = np.clip(x_blue, 0, 255)

    resultImg = reconstructImg(indexes, x_red, x_green, x_blue, targetImg)
    return resultImg
