def getLevDistance(s1, s2):
    if len(s1) * len(s2) == 0:
        return max(len(s1), len(s2))
    D = [[0] * (len(s2) + 1) for i in range(len(s1) + 1)]
    for i in range(1, len(D[0])):
        D[0][i] = i
    for i in range(1, len(D)):
        D[i][0] = i
    for i in range(1, len(D)):
        for j in range(1, len(D[i])):
            replace = 0
            if s1[i - 1] != s2[j - 1]:
                 replace = 1
            D[i][j] = min(D[i - 1][j] + 1, D[i - 1][j - 1] + replace, D[i][j - 1] + 1)
    return D[-1][-1]
                
def findMinWindow(s, t):
    """
    Finds the minimum window in s which will contain all the characters in t.
    """
    M = {}
    for c in t:
        if c in M:
            M[c] += 1
        else:
            M[c] = 1
    start, end, startF = 0, 0, 0
    hit = False
    count, minL = len(t), len(s)
    while start < len(s):
        if end < len(s) and count > 0:
            if s[end] in M:
                if M[s[end]] > 0:
                    count -= 1
                M[s[end]] -= 1
            end += 1
        else:
            if s[start] in M:
                if M[s[start]] == 0:
                    count += 1
                M[s[start]] += 1
            start += 1
        if end - start <= minL and count == 0:
            minL = end - start
            hit = True
            startF = start
    if hit :
        return s[startF : startF + minL]
    else:
        return ""

def isInterleave(s1, s2, s3):
    """
    Determines if s3 could be formed by the interleaving of s1 and s2.
    """
    if len(s1) + len(s2) != len(s3):
        return False
    else:
        T = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]
        T[0][0] = True
        for i in range(0, len(s1)):
            T[i + 1][0] = T[i][0] and s1[i] == s3[i]
        for j in range(0, len(s2)):
            T[0][j + 1] = T[0][j] and s2[j] == s3[j]
        for i in range(0, len(s1)):
            for j in range(0, len(s2)):
                T[i + 1][j + 1] = (T[i][j + 1] and s1[i] == s3[i + j + 1]) or (T[i + 1][j] and s2[j] == s3[i + j + 1])
                
        return T[-1][-1]

def countDistinctSubseq(s, t):
    """
    Counts the number of distinct subsequences in s which equals t.
    """
    T = [[0] * (len(t) + 1) for i in range(len(s) + 1)]
    for i in range(len(T)):
        T[i][0] = 1
    for i in range(1, len(T)):
        for j in range(1, min(len(T[0]), i + 1)):
            if s[i - 1] == t[j - 1]:
                T[i][j] = T[i - 1][j - 1] + T[i - 1][j]
            else:
                T[i][j] = T[i - 1][j]
    return T[-1][-1]

def compareVersion(version1, version2):
    """
    Compares the version numbers. Returns 1 if version1 > version2
    and 0 otherwise.
    """
    i, j = 0, 0
    v1, v2 = version1, version2
    while i < len(v1) or j < len(v2):
        n1, n2 = 0, 0
        while i < len(v1) and v1[i] != '.':
            n1 = n1 * 10 + int(v1[i])
            i += 1
        while j < len(v2) and v2[j] != '.':
            n2 = n2 * 10 + int(v2[j])
            j += 1
        if n1 > n2:
            return 1
        elif n2 > n1:
            return -1
        else:
            i += 1
            j += 1
    return 0

def removeInvalidParentheses(string, targets = "()"):
    """
    Removes the minimum number of invalid parentheses in order to make
    the input string valid. Returns all possible results. Can be used
    to remove othre brackets too.
    Parameters
    """
    def isValid(string, left, right):
        count = 0
        for i in range(len(string)):
            if count < 0:
                return False
            if string[i] == left:
                count += 1
            elif string[i] == right:
                count -= 1
        return count == 0
    assert targets in ("()", "{}", "[]", "<>")
    left, right = targets[0], targets[1]
    if isValid(string, left, right):
        return [string]
    result = []
    Q = [(string, 0, right)]
    while len(Q) > 0:
        current = Q.pop(0)
        S = current[0]
        start = current[1]
        last = current[2]
        for i in range(start, len(S)):
            if (S[i] == left or S[i] == right) and (i == start or S[i - 1] != S[i]) and not (last == left and S[i] == right):
                newS = S[ : i] + S[i + 1 :]
                if isValid(newS, left, right):
                    result.append(newS)
                elif len(result) == 0:
                    Q.append((newS, i, S[i]))
    return result