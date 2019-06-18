# 1）A太小，A+3*MAX<target ,跳过这个A，A+1
#
# 2）A太大，4*A >=target, 那么A的取值到此为止了，break

class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        l = len(nums)
        res = []
        if l < 4:
            return res
        nums.sort()
        max_num = nums[-1]

        # 4SUM
        for i in range(l - 3):
            a = nums[i]
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if a + 3 * max_num < target:
                continue
            elif 4 * a == target:
                if i + 3 < l and nums[i + 3] == a:
                    res.append([a, a, a, a])
                break
            elif 4 * a > target:
                break

            # 3SUM
            target_3 = target - a
            j = i + 1
            for j in range(i + 1, l - 2):
                b = nums[j]
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                if b + 2 * max_num < target_3:
                    continue
                elif 3 * b == target_3:
                    if j + 2 < l and nums[j + 2] == b:
                        res.append([a, b, b, b])
                    break
                elif 3 * b > target_3:
                    break

                # 2SUM
                target_2 = target_3 - b   # 二分
                left, right = j + 1, l - 1
                while left < right:
                    sum_2 = nums[left] + nums[right]
                    if sum_2 == target_2:
                        res.append([a, b, nums[left], nums[right]])
                        while left < right and nums[left + 1] == nums[left]:
                            left += 1
                        left += 1
                        while left < right and nums[right - 1] == nums[right]:
                            right -= 1
                        right -= 1
                    elif sum_2 < target_2:
                        left += 1
                    else:
                        right -= 1

        return res

















