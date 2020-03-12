# 寻找字符串中唯一的元素
#
# 对于唯一值的筛查，首先应该想到对于set的利用，set可以帮助我们快速的筛查重复的元素
# # set不仅可以对字符串，而且还可以针对列表进行筛查


str1 = 'aabbzdbzzcc'
print(set(str1))
print(''.join(set(str1)))


str2 = [33, 22, 33, 33, 1, 22]
print(set(str2))
print(list(set(str2)))
