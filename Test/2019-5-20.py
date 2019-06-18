# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
#
# 有效字符串需满足：
#
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 注意空字符串可被认为是有效字符串。

list_a = ['{', '(', '[']
str_b = '({{})}'
c = list(str_b)
print(c)


def function(str_a):
    dict_a = {'{': '}', '(': ')', "[": "]"}
    if len(str_a) > 1:
        if str_a[0] in dict_a.keys() and str_a[-1] == dict_a[str_a[0]]:
            del str_a[0]
            del str_a[-1]
        function(str_a)

    if len(str_a) == 0:
        return 1
    else:
        return -1



print(function(c))
