def find_brute(T, P):
    n, m = len(T), len(P)
    for i in range(n-m+1):
        k = 0
        while k < m and T[i+k] == P[k]:    #T[i+k] i的作用是选择T对O对比的起始点
            k += 1
            if k == m:
                return i
    return -1


find_brute('abcefabcde', 'abcd')



