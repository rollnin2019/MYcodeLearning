
# 在一条环路上有 N 个加油站，其中第 i 个加油站有汽油 gas[i] 升。
#
# 你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站
# 需要消耗汽油 cost[i] 升。你从其中的一个加油站出发，开始时油箱为空。
#
# 如果你可以绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1。
#
# 说明:
#
# 如果题目有解，该答案即为唯一答案。
# 输入数组均为非空数组，且长度相同。
# 输入数组中的元素均为非负数。


def canCompleteCircuit( gas, cost):
    temp_sum_gas = 0
    temp_sum_cost = 0
    ans = 0
    if sum(gas) < sum(cost):
        return -1
    for i in range(len(gas)):
        temp_sum_gas += gas[i]
        temp_sum_cost += cost[i]
        # 如果一个数组的总和非负，
        # 那么一定可以找到其中找到一个点开始，累加和一直都是非负的
        if temp_sum_gas < temp_sum_cost:
            temp_sum_gas = 0
            temp_sum_cost = 0
            ans = i + 1
    return ans


gas = [5, 1, 2, 3, 4]
cost = [4, 4, 1, 5, 1]
print(canCompleteCircuit(gas, cost))
