from copy import deepcopy

#============================== List ===============================#

def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

    
def findKthLargest(L, k):
    def quickselect(L, start, end, k):
        if start == end:
            return L[start]
        pivot = random.randint(start, end)
        swap(L, pivot, end)
        i = start
        for j in range(start, end):
            if L[j] >= L[end]:
                swap(L, i, j)
                i += 1
        swap(L, i, end)
        if i == k:
            return L[i]
        elif i < k:
            return quickselect(L, i + 1, end, k)
        else:
            return quickselect(L, start, i - 1, k)
    return quickselect(L, 0, len(L) - 1, k - 1)

def removeDuplicates(L):
    """
    Removes the duplicates from L such that each element appear only once.
    Assuming that L is sorted.
    """
    if len(L) == 0:
        return 0
    i = 0
    for j in range(len(L)):
        if L[i] != L[j]:
            i += 1
            L[i] = L[j]
    return L[:i + 1]
    
def removeDuplicates2(L):
    """
    Removes the duplicates from L such that each element appear once or twice.
    Assuming that L is sorted.
    """
    i = 0
    for j in range(len(L)):
        if j < 2 or L[j] != L[i - 2]:
            L[i] = L[j]
            i += 1
    return L[:i]
    
def findInRoratedArray(L, target):
    """
    Finds the first appearance of a target in L where elements are
    sorted but rotated. L might contain duplicates.
    """
    if len(L) == 0:
        return None
    n = len(L)
    pivot = 0
    for i in range(len(L) - 1):
        if L[i] > L[i + 1]:
            pivot = i + 1
            break
    i, j = 0, n - 1
    while i < j:
        mid = (i + j) // 2
        rotatedMid = (mid + pivot) % n
        if L[rotatedMid] < target:
            i = mid + 1
        else:
            j = mid
    if L[(i + pivot) % n] == target:
        return (i + pivot) % n
    else:
        return None

def minSubArrayLen(s, L):
    """
    Finds the minimal length of a contiguous subarray of which the
    sum >= s. Assuming that the array only contains positive integers.
    """
    i, j = 0, 0
    sum = 0
    minL, result = len(L) + 1, []
    while j < len(L):
        while j < len(L) and sum < s:
            sum += L[j]
            j += 1
        while i < j and sum >= s:
            if j - i < minL:
                minL = j - i
                result = L[i : j + 1]
            sum -= L[i]
            i += 1
    return result

def fill(source, destination, start, end):
    """
    Fills the destination list from index start to index end (inclusive)
    with elements from source.
    Parameters
    ----------
    source, destination : List
    start, end : int
    Returns
    -------
    None
    """
    if end < start:
        print("[def fill] end < start")
        sys.exit()
    elif len(source) != end - start + 1:
        print("[def fill] len(source) = " + str(len(source)) +\
                " while (end - start + 1) = " + str(end - start + 1))
        sys.exit()
    elif end >= len(destination):
        print("[def fill] end >= len(destination)")
        sys.exit()
    else:
        for i in range(start, end + 1):
            destination[i] = source[i - start]



#========================== End of Section =========================# 
#=========================== Permutations ==========================#

def getAllPermutations(L, unique = False):
    """
    Finds a list of all permutations of L.
    Parameters
    ----------
    L : array-like
    unique: boolean
        Indicates whether or not only unique permutations are returned.
    """
    def buildList(result, current, L, unique):
        if len(L) == 0:
            result.append(deepcopy(current))
        else:
            known = []
            for i in range(len(L)):
                if not L[i] in known:
                    if unique:
                        known.append(L[i])
                    current.append(L[i])
                    buildList(result, current, L[:i] + L[i + 1:], unique)
                    current.pop()
    result = []
    buildList(result, [], L, unique)
    return result
    
def getKthPermutation(n, k):
    """
    Given n and k, return the kth permutation sequence of
    [1, 2, 3, ..., n].
    """
    candidates = [str(i + 1) for i in range(n)]
    binSizes = [1] * n
    for i in range(1, n):
        binSizes[i] = binSizes[i - 1] * i
    result = ""
    k -= 1 
    for i in range(n):
        currentIndex = int(k / binSizes[-1 - i])
        k %= binSizes[-1 - i]
        result += candidates[currentIndex]
        candidates = candidates[:currentIndex] + candidates[currentIndex + 1 :]
    return result

#========================== End of Section =========================# 
#============================= Subsets =============================#

def findSubsets(L):
    """
    Finds the power set of L. Assuming every elemet is unique.
    """
    def buildList(result, current, L, start, k):
        if k == 0:
            result.append(current[:])
        else:
            for i in range(start, len(L)):
                current.append(L[i])
                buildList(result, current, L, i + 1, k - 1)
                current.pop()
    result = []
    for k in range(len(L) + 1):
        buildList(result, [], L, 0, k)
    return result
    
def findSubsetsWithDuplicates(L):
    """
    Finds the power set of L, which might contains duplicates.
    """
    def buildList(result, current, N, start, counts, k):
        if k == 0:
            result.append(current[:])
        else:
            for i in range(start, len(N)):
                for j in range(counts[N[i]]):
                    current.append(N[i])
                    buildList(result, current, N, i + 1, counts, k - 1)
                for j in range(counts[N[i]]):
                    current.pop()
    counts = {}
    N = []
    for n in L:
        if n in counts:
            counts[n] += 1
        else:
            N.append(n)
            counts[n] = 1
    result = []
    for k in range(len(L) + 1):
        buildList(result, [], N, 0, counts, k)
    return result

def maxProductSubarray(L):
    """
    Finds the contiguous subarray within an array (containing at least
    one number) which has the largest product.
    """
    if len(L) == 0:
        return None
    CPm, CPM, MP = L[0], L[0], L[0]
    start, end = 0, 1
    startCurrent, endCurrent = 0, 1
    for i in range(1, len(L)):
        n = L[i]
        if n < 0:
            temp = CPm
            CPm = CPM
            CPM = temp
        CPm = min(CPm * n, n)
        if CPM * n > n:
            CPM = CPM * n
        else:
            CPM = n
            startCurrent = i
        endCurrent = i + 1
        if CPM > MP:
            MP = CPM
            start, end = startCurrent, endCurrent
    return L[start : end]
    
def findPeakElement(L):
    """
    Finds a peak element in L. An element is a peak element if it is
    greater than its neighbors. Assuming that for any valid i,
    L[i] != L[i + 1].
    """
    n = [-sys.maxsize] + L + [-sys.maxsize]
    i, j = 0, len(n) - 1
    while i < j:
        mid = (i + j) // 2
        if n[mid] > n[mid - 1] and n[mid] > n[mid + 1]:
            return mid - 1
        elif n[mid - 1] < n[mid] < n[mid + 1]:
            i = mid + 1
        else:
            j = mid
    return i

#========================== End of Section =========================#
#============================= Sampling ============================#

def topKFrequent(L, k):
    """
    Finds the top k frequent elements in L.
    """
    bucket = [[] for i in range(len(L) + 1)]
    count = {}
    for n in L:
        count[n] = 1 + count.get(n, 0)
    for n in count:
        bucket[count[n]].append(n)
    result = []
    i = len(bucket) - 1
    while i >= 0 and len(result) < k:
        result += bucket[i]
        i -= 1
    return result

def canPartitionEqually(L):
    """
    Determines if L can be partitioned into two subsets such that
    the sum of elements in both subsets is equal. Assuming that
    L is non-empty and contains only positive integers.
    """
    assert len(L) > 0
    S = sum(L)
    if S % 2 == 1:
        return False
    S = S // 2
    T = [False] * (S + 1)
    T[0] = True
    for i in range(len(L)):
        for j in range(S, L[i] - 1, -1):
            T[j] = T[j] or T[j - L[i]]
    return T[-1]

#========================== End of Section =========================#