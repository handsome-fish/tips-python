# 字符串翻转

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
