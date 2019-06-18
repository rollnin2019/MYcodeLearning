#穷举算法
def function_findstrsame_1(P, T):
    _length_P = len(P)
    _length_T = len(T)
    for i in range(_length_P):
        k = 0
        while k < _length_T and P[i+k] == T[k]:
            k += 1
            if k == _length_T:
                return i
    return False


print(function_findstrsame_1("abcdfsadjksajhdsahd","jks"))













