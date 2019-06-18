
class Poke:
    target = '12345678910111213'
    poke = []

    def get__poke(self):
        """
        得到扑克序列 0为王
        :return:
        """
        for i in range(5):
            n = int(input('plz input poke number:'))
            if n != 0:
                Poke.poke.append(n)
        return Poke.poke

    def list_to_str(self, a):
        """
        将排列好的列表中的数字转换为字符串 使用 str1 in str2判断
        :param a:
        :return:
        """
        _str_a = ''
        for j in a:
            _str_a += str(j)
        return _str_a

    def function_two_joker(self):
        """
        两张大王的情况
        :param a:参与比较的列表 只有3个变量
        :return:
        """
        global s1
        for s1 in range(1, 14):
            _str = Poke.poke
            _str.append(s1)
            for s2 in range(1, 14):
                _str.append(s2)
                _str.sort()
                if self.list_to_str(_str) in self.target:
                    return True
                else:
                    _str.remove(s2)

            _str.remove(s1)
        else:
            return False

    def function_one_joker(self, ):
        """
        只有一张大王的情况
        :param a: 参与比较的列表 只有4个变量
        :return:
        """
        _str = Poke.poke
        for s2 in range(1, 14):
            _str.append(s2)
            _str.sort()
            if self.list_to_str(_str) in self.target:
                return True
            else:
                _str.remove(s2)
        else:
            return False

    def simple_question(self):
        """
        没有大王的情况 将列表排序后转换成为字符串后比较
        :param a:
        :return:
        """
        a = Poke.poke
        a.sort()
        if self.list_to_str(a) in self.target:
            return True
        else:
            return False


p1 = Poke()
p1.get__poke()
print(p1.simple_question())



