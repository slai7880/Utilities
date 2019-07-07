"""
Sha Lai
This script contains utility functions used in various problems.
"""

import numpy as np
import os, sys
import random
from copy import deepcopy
 
#============================== Matrix =============================#

def getSpiralOrder(matrix):
    """
    Returns the elements in matrix in spiral order.
    Parameters
    ----------
    matrix : List[List] or numpy matrix
    Returns
    -------
    result : List
        A list of elements in matrix but in spiral order.
    """
    if isinstance(matrix, np.matrix):
        matrix = matrix.tolist()
    if len(matrix) == 0:
        return []
    else:
        m, n = len(matrix) - 1, len(matrix[0])
        result = [0] * (len(matrix) * len(matrix[0]))
        count = 0
        current = [0, -1]
        dir = 1
        while count < len(result):
            for i in range(n):
                current[1] += dir
                result[count] = matrix[current[0]][current[1]]
                count += 1
            n -= 1
            for i in range(m):
                current[0] += dir
                result[count] = matrix[current[0]][current[1]]
                count += 1
            m -= 1
            dir *= -1
        return result

def generateSpiralMatrix(n):
    """
    Generate a square matrix filled with elements from 1 to n^2 in spiral order.
    Parameters
    ----------
    n : int
    Returns
    -------
    result : List[List[int]]
    """
    result = [[0] * n for i in range(n)]
    current = [0, -1]
    dir = 1
    nM, nN = n - 1, n
    count = 1
    while count <= n**2:
        for i in range(nN):
            current[1] += dir
            result[current[0]][current[1]] = count
            count += 1
        nN-= 1
        for i in range(nM):
            current[0] += dir
            result[current[0]][current[1]] = count
            count += 1
        nM -= 1
        dir *= -1
    return result

def setZeroes(matrix):
    """
    Sets the entire row i and column j or matrix to be zeroes if entry
    matrix[i, j] is zero.
    Parameters
    ----------
    matrix : List[List[float]]
    Returns
    -------
    None
    """
    if len(matrix) > 0:
        m, n = len(matrix), len(matrix[0])
        firstRow, firstCol = False, False
        for i in range(m):
            if matrix[i][0] == 0:
                firstCol = True
        for j in range(n):
            if matrix[0][j] == 0:
                firstRow = True
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0
        if firstRow:
            for j in range(n):
                matrix[0][j] = 0
        if firstCol:
            for i in range(m):
                matrix[i][0] = 0

#========================== End of Section =========================#
#=========================== Dictionaries ==========================#

def mergeDictionaries(dictionaries, silenceMode = True):
    """Merges a list of dictionaries. If there is a repeated key, the
    value will be the one that comes later.
    """
    result = {}
    size = 0
    for d in dictionaries:
        size += len(d)
        for key in d:
            result[key] = d[key]
    if not silenceMode:
        print("Merged size = " + str(len(result)) + "  Original total size = " + str(size))
    return result
    
#========================== End of Section =========================#
#========================== Transformation =========================#

def categorize(L):
    count = 0
    M = {}
    for i in L:
        if not i in M:
            M[i] = count
            count += 1
    return [M[i] for i in L]

def getBinaryVectors(L, rangeTuple = None):
    """
    Given a numpy array of integers, for each of the integers, constructs
    a vector representation of that integer. Returns a numpy matrix containing
    these results.
    Parameters
    ----------
    L : numpy array
    rangeTuple : (int, int)
        Must be in the form (min, max).
    Returns
    -------
    result : numpy matrix
    """
    if rangeTuple is None:
        rangeTuple = (min(L), max(L))
    (m, M) = rangeTuple
    result = np.zeros((len(L), M - m + 1))
    for i in range(len(L)):
        result[i, L[i] - m] = 1
    return result

#========================== End of Section =========================#