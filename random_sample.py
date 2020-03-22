# 随机采样
# 使用random.sample()函数，可以从一个序列中选择n_samples个随机且独立的元素

import random

string = "i love python"
lst = ['p', 'y', 't', 'h', 'o', 'n']

n_samples = 3
print(random.sample(string, n_samples))
print(random.sample(lst, n_samples))
