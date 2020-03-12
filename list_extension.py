# 基于列表的扩展
#
# 基于列表的扩展，可以充分利用列表的特性和python语法的简洁性，来产生新的列表
# 或者将嵌套的列表进行展开


list1 = [2, 3, 4, 5]
print([2*i for i in list1])


# 列表的展开
list2 = [[1, 2, 3], [2, 3], [4], [1, 2]]
print([i for j in list2 for i in j])
