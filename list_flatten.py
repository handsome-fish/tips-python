# 将列表展开
#
# 方法1中 ，我们调用的是iteration_utilities 中的deepflatten函数
# 方法2中，采用递归的方法，我们自己来实现复杂列表的展平，便可以得到展开后的列表


lst = [[12, 2, 3], [1, 2, [4, 5, [5]]], 5, [3]]


# 方法一
from iteration_utilities import deepflatten as df


print(list(df(lst)))


# 方法二
def flatten(lst):
    res_list = []
    for i in lst:
        if type(i) is list:
            res_list.extend(flatten(i))
        else:
            res_list.append(i)
    return res_list


print(flatten(lst))
