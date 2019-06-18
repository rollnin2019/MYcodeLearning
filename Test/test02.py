A = [5, 2, 7, 28, 4, 3, 11, 19]


def function(list_a):
    list_right = []
    list_left = []
    if len(list_a) >= 2:
        _mid = list_a[len(list_a) // 2]
        list_a.remove(_mid)
        for i in list_a:
            if i > _mid:
                list_right.append(i)
            else:
                list_left.append(i)
        return function(list_left) + [_mid] + function(list_right)
    else:
        return list_a


print(function(A))













