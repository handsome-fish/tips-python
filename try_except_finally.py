# 使用try-except-finally模块
# 当我们在执行程序时，可能会遇到某些不可预知的错误，使用try-except可以帮助我们去捕获这些错误，然后输出提示
# 注意，如果需要程序无论是否出错，都要执行一些程序的化，需要利用finally来实现


def if_a_list(a, b):
    try:
        a.append(b)
    except AttributeError as e:
        print("'a' 不是一个列表!")
    else:
        print(a)
    finally:
        print("程序结束")
    print("===============================")


a = 2
b = 4
if_a_list(a, b)
a = [2]
if_a_list(a, b)
