def insert_sort(A):
    for i in range(1, len(A)):
        _num = A[i]
        while i > 0 and _num < A[i-1]:
            A[i] = A[i-1]
            i = i - 1
        A[i] = _num
    return A










