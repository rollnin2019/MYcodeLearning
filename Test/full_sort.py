list_b = []


def number(A, position, n):
    if position == n:
        print(A)
        list_b.append(A)

    for i in range(position, n):
        A[i], A[position] = A[position], A[i]
        number(A, position + 1, n)
        A[i], A[position] = A[position], A[i]


number(['a', 'b',  'a'], 0, 3)



