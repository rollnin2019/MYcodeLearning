def findsmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionsort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findsmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


print(selectionsort([2, 7, 1, 5, 8, 9, 24]))
