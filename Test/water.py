list_a = [1, 8, 6, 2, 5, 4, 8, 3, 7]

left = 0
right = len(list_a) - 1
_max = 0
while left < right:
    _max = max(_max, (right - left) * min(list_a[right], list_a[left]))
    if list_a[right] > list_a[left]:
        left += 1
    else:
        right -= 1

print(_max)
