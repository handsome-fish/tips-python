# 使用enumerate() 函数来获取索引-数值对
# enumerate() 函数用于将一个可遍历的数据对象(如上图的列表，字符串)组合为一个索引序列


def enum(obj):
    for i, j in enumerate(obj):
        print(i, j)
    print("==================================")


str = "Python"
list = [1, 34, 32, 13]
enum(str)
enum(list)
