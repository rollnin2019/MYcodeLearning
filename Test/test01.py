def insertion_sort(A):
    for k in range(1, len(A)):
        cur = A[k]
        j = k
        while j > 0 and A[j-1] > cur:
            A[j] = A[j-1]
            j -= 1
        A[j] = cur
    return A


def function_sort(A):
    for i in range(1, len(A)):
        _num1 = A[i]  # 在while循环中一个不会随着k变化的定值
        k = i  # ?
        # while k > 0 and A[k] < A[k-1]:  k>k-1时不进行循环节省时间
        while k > 0 and _num1 < A[k - 1]:
            A[k] = A[k - 1]  # [7,6]变成[7,7]  [11,12,15,10]--[11,12,15,15]
            k = k - 1    # 控制指针向前推进
        A[k] = _num1  # [7,7]变成[6,7] 将更小的向后移动  找到不大于_num1的数字  这个数字之后的全部被排列
    #        ↑←完成插入的过程
    return A


print(function_sort([1, 4, 13, 19, 9, 1]))
