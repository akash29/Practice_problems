def isMatch(s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    T = [[False] * (len(p) + 1) for i in range(len(s)+1)]
    T[0][0] = True

    for i in range(1,len(p)+1):
        if p[i-1] == '*':
            T[0][i] = T[0][i-1]


    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            if s[i - 1] == p[j - 1] or p[j - 1] == '?':
                T[i][j] = T[i - 1][j - 1]
            elif p[j - 1] == '*':
                T[i][j] = T[i][j - 1] or T[i-1][j]

            else:
                T[i][j] = False

    print(T[len(s)][len(p)])

isMatch('aab','c*a*b')