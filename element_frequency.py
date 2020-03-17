# 统计列表中元素的频率
# 直接调用collections中的Counter类来统计元素的数量
# 也可以自己来实现这样的统计
# 但是从简洁性来讲，还是以Counter的使用比较方便

# 方法一
from collections import Counter

lst = [2, 1, '3', 3, 3, 2, 3, 1, 5, 6]
count = Counter(lst)
print(count)
print(count[2])
print(count.most_common(2))


# 方法二
dic = {}
for i in lst:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
print(max(dic, key=lambda x:dic[x]))
