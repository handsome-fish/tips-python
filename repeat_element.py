# 将元素进行重复
#
# 将元素进行重复，可以采用“乘法”的形式，直接乘以原来的元素
# 也可以采用“加法”的形式，更方便理解


def multi_repeat(str_rep, n):
    """
    乘法表述
    str_rep: str to repeat
    n: number of repetition
    """
    return str_rep * n


def plus_repeat(str_rep, n):
    """
    加法表述
    str_rep: str to repeat
    n: number of repetition
    """
    if type(str_rep) is str:
        res_str = ''
        for i in range(n):
            res_str += str_rep
        return res_str
    elif type(str_rep) is list:
        res_list = []
        for i in range(n):
            res_list.extend(str_rep)
        return res_list
    else:
        return 'Error: str_rep should be str or list'


str_rep = '1 2 3 '
list_rep = [1, 's', (5,'3')]
n = 2
print(multi_repeat(str_rep, n))
print(multi_repeat(list_rep, n))
print(plus_repeat(str_rep, n))
print(plus_repeat(list_rep, n))
