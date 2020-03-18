# 将数字字符串转化为数字列表
# 方法1利用的map函数，map函数可以将str19中的每个元素都执行int函数，其返回的是一个迭代器，利用list函数来将其转化为列表的形式
# 注意，在python2中执行map函数就会直接返回列表，而python3做了优化，返回的是迭代器，节省了内存

num_str = "2353255"

# 方法一
list1 = list(map(int, num_str))
print(list1)
print("==============================================")

# 方法二
list2 = [int(i) for i in num_str]
print(list2)
