# 给定一个整数数组 nums
# 和一个目标值 target，
# 请你在该数组中找出和为目标值的
# 那 两个 整数，并返回他们的数组下标。

def twoSum(nums, target):
    dict_aim = {}
    A = []
    for i in nums:
        if i not in dict_aim.values():
            dict_aim[i] = target - i
        else:
            if i == target - i:
                A.append(nums.index(i))
                A.append(len(nums[:(nums.index(i) + 1)]) + nums[nums.index(i) + 1:].index(i))
                break
            else:
                A.append(nums.index(target - i))
                A.append(nums.index(i))
                break
    return A


c = twoSum([3, 2, 3], 6)
print(c)
