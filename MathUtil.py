import numpy as np
import os, sys
import random
from copy import deepcopy
import bisect

def gcd(a, b, recursion = True):
    """
    Returns the greatest common divider of a and b.
    """
    if recursion: # one way to solve it is by recursion
        if a == b:
            return a
        elif a > b:
            return gcd(a - b, b, True)
        else:
            return gcd(a, b - a, True)
    else: # there exists an iterative solution as well
        while a != b:
            if a > b:
                a -= b
            else:
                b -= a
        return a
    
        
def findModes(L):
    maxCount = max([L.count(i) for i in set(L)])
    return [i for i in set(L) if L.count(i) == maxCount]
    
def countPrimes(n):
    """
    Counts the number of primes up to n.
    """
    P = [True] * n
    P[0], P[1] = False, False
    i = 2
    while i**2 < n:
        if P[i]:
            j = i
            while j * i < n:
                P[i * j] = False
                j += 1
        i += 1
    return sum(P)
    
def countSquares(n):
    """
    Finds the minimum number of perfect square numbers that sum to n.
    Assuming that n is an integer.
    """
    assert isinstance(n, int)
    if n < 0:
        return 0
    result = [0] * (n + 1)
    i = 1
    while i <= n:
        result[i] = i + 1
        j = 0
        while j**2 <= i:
            result[i] = min(result[i], 1 + result[i - j * j])
            j += 1
        i += 1
    return result[n]
    
def integerBreak(n):
    """
    Breaks a positive integer n into the sum of at least two positive
    integers such that their product is maximized.
    """
    assert n > 0 and isinstance(n, int)
    T = [0] * n
    T[0], T[1] = 1, 1
    for i in range(2, n):
        M = 1
        if i % 2 == 1:
            M = max((i // 2 + 1)**2, T[i // 2]**2)
        else:
            M = max((i // 2 + 1) * (i // 2), T[i // 2] * T[i // 2 - 1])
        for j in range(int(np.ceil(i / 2))):
            M = max(M, max(T[j], j + 1) * max(T[i - 1 - j], i - j))
        T[i] = M
    return T[n - 1]
    
def nChooseK(n, k):
    assert k > 0 and n >= k and isinstance(n, int) and isinstance(k, int)
    numerator = 1
    denominator = 1
    for i in range(k + 1, n + 1):
        numerator *= i
    for i in range(1, n - k + 1):
        denominator *= i
    return numerator / denominator
    
def argmax(target, candidates, method):
    optimalIndex, optimalDistance = 0, -sys.maxsize
    for i in range(len(candidates)):
        distance = method(target, candidates[i])
        if distance > optimalDistance:
            optimalDistance = distance
            optimalIndex = i
    return optimalIndex
    
def argmin(target, candidates, method):
    optimalIndex, optimalDistance = 0, sys.maxsize
    for i in range(len(candidates)):
        distance = method(target, candidates[i])
        if distance < optimalDistance:
            optimalDistance = distance
            optimalIndex = i
    return optimalIndex

class WeightedRandomSelector:
    """Given a list of positive integers as weights, randomly
    picks an index of the list based on the weights.
    """
    def __init__(self, weights):
        assert not weights is None and len(weights) > 0
        for i in range(len(weights)):
            assert weights[i] >= 0 and int(weights[i]) == weights[i]
        self.accumulated = [0] * len(weights)
        self.accumulated[0] = weights[0]
        for i in range(1, len(weights)):
            self.accumulated[i] = self.accumulated[i - 1] + weights[i]
    
    def pickIndex(self):
        target = random.randint(1, self.accumulated[-1])
        return bisect.bisect_left(self.accumulated, target)