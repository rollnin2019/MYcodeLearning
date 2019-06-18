# 剪枝搜索
def function(A, low, high, target):
    _mid = (low + high) // 2
    if low > high:
        return False
    elif A[_mid] == target:
        return _mid
    elif A[_mid] < target:
        return function(A, _mid + 1, high, target)
    elif A[_mid] > target:
        return function(A, low, _mid - 1, target)


print(function([1, 2, 3, 4, 5], 0, 5, 1))


































