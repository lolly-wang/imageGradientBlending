'''
  File name: getSolutionVect.py
  Author: Luoli Wang
  Date created: Sep 25,2019
'''
import numpy as np
from scipy import signal

def getSolutionVect(indexes, source, target, offsetX, offsetY):
    N = np.amax(indexes)

    edgeVect = np.zeros(N)
    for index in range(1, N + 1):
        m, n = np.where(indexes == index)
        i = np.int(m[0])
        j = np.int(n[0])
        if indexes[i + 1, j] == 0 : edgeVect[index - 1] += target[i + 1, j]
        if indexes[i - 1, j] == 0 : edgeVect[index - 1] += target[i - 1, j]
        if indexes[i, j + 1] == 0 : edgeVect[index - 1] += target[i, j + 1]
        if indexes[i, j - 1] == 0 : edgeVect[index - 1] += target[i, j - 1]

    kernel = np.array(
        [[0, -1, 0],
         [-1, 4, -1],
         [0, -1, 0]])
    srcH, srcW = source.shape
    tarH, tarW = target.shape

    Div_source = np.zeros_like(indexes)
    div_src = signal.convolve2d(source, kernel, 'same')
    Div_source[offsetX:offsetX + srcH, offsetY:offsetY + srcW] = div_src

    SolVectorb = np.zeros(N)
    cnt = 0
    for i in range(0, tarH):
        for j in range(0, tarW):
            if indexes[i, j] > 0:
                SolVectorb[cnt] = Div_source[i, j]
                cnt += 1

    combined_SolVector = SolVectorb + edgeVect
    return combined_SolVector


