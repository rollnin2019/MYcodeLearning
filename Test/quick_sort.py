def function_a(A):
    if len(A) >= 2:
        left = []
        right = []
        _mid = A[len(A) // 2]
        A.remove(_mid)
        for i in A:
            if i > _mid:
                right.append(i)
            else:
                left.append(i)
        return function_a(left) + [_mid] + function_a(right)
    else:
        return A


print(function_a([2, 1, 3, 7, 5, 6, 9, 11]))
