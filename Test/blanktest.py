# 在未排序的数组中找到第 k 个
# 最大的元素。请注意，你需要找的是数组排序
# 后的第 k 个最大的元素，而不是第 k 个不同的元素。
def findKthLargest(A, k):
    if A == []:
        return False
    aim = k
    C = []
    A.sort()
    start = A[0]
    number = 1
    C.append((A[0], 1))
    for i in A:
        if i == start and k > 1:
            k -= 1
        if i >= start:
            number = number + 1
            C.append((i, number))
            start = i
    if aim > len(C):
        return C[len(C) - k][0]
    else:
        return C[len(C)-aim][0]

A = [3,3,3,3,3,3,3,3,3]
k = 8
c =findKthLargest(A, k)
print(c)