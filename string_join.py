# 字符串合并
#
# 将列表中的字符串合并为字符串
# 可以与字符串分割结合，来去除字符串中不想留下的项


list = ['i', 'love', 'python']
print(' '.join(list))


# 去除字符串中不需要的字符
import re
str = '            i^%*&love    ^*&python  '
print(' '.join(re.split(r'\W+', str.strip())))





