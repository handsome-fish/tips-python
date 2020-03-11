# 字符串翻转
# 首先最简单的方法就是利用切片的操作，来实现翻转，
# 其次可以利用reduce函数来实现翻转，在python3中，reduce函数需要从functools中进行导入


# method1
def method1(str):
    return str[::-1]


# method2
from functools import reduce
def method2(str):
    return reduce(lambda x, y: y+x, str)


if __name__ == '__main__':
    str = 'i love python.'
    print('method1: ' + method1(str))
    print('method2: ' + method2(str))
