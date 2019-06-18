
# 在一个字符串(0<=字符串长度<=10000，
# 全部由字母组成)中找到第一个只出现一次的字符,
# 并返回它的位置, 如果没有则返回 -1（
# 需要区分大小写）
_str = 'daebcdabc'


def method_name(_str):
    list_a = []
    for i in range(len(_str)):
        for k in range(i + 1, len(_str)):
            if _str[i] == _str[k]:
                list_a.append(_str[i])
                break
        if _str[i] not in list_a:
            return i
    else:
        return -1


print(method_name(_str))












