# def find_same_number(A):
#     for i in range(0, len(A)):
#         _num1 = A[i]
#         k = i + 1
#         while k < len(A):
#             if A[k] == _num1:
#                 print(A[i])
#                 return
#             k = k + 1
#
#     return
#
#
# find_same_number([1, 2, 3, 9, 9, 9])


A = [1, 2, 3, 9, 9, 9]
list_a = []
for i in A:
    if i not in list_a:
        list_a.append(i)
    else:
        print(i)
        break





