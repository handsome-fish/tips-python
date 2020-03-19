# 代码执行消耗时间
# 利用time()函数，在核心程序开始前记住当前时间点
# 然后在程序结束后计算当前时间点和核心程序开始前的时间差
# 可以帮助我们计算程序执行所消耗的时间


import time
start = time.time()

# 代码块
num = 0
for i in range(1000000):
    num = i

# 打印消耗时间
print("共消耗时间: " + str(time.time()-start), "s")
