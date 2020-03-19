# 检查对象的内存占用情况
# 在python中可以使用sys.getsizeof来查看元素所占内存的大小
# 关于这个值是怎么算出来的，有待研究


import sys

str1 = "a"
str2 = "python"
num = 123
lst = [1, "2", "pycharm"]

print(sys.getsizeof(str1))
print(sys.getsizeof(str2))
print(sys.getsizeof(num))
print(sys.getsizeof(lst))
