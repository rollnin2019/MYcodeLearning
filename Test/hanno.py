def func(n, A, B, C):
    if n == 1:
        print(A + " -- >" + B)
    else:
        func(n - 1, A, C, B)
        print(A + " -- >" + B)
        func(n - 1, C, B, A)


func(3, A='A', B='B', C='C')