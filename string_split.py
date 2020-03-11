# 字符串拆分
#
# 字符串的拆分可以直接利用split函数，进行实现，返回的是列表
# 而strip函数用于移除字符串头尾指定的字符（默认为空格或换行符）
# 另一种分割是re.split，需要导入re包，适用复杂情况分割，支持多种分隔符同时分割，


str1 = 'i love python'
str2 = 'i/love/python'
str3 = '  i love python   ' \
       ''
print(str1.split())  # 默认按空格拆分，返回的是列表
print(str2.split('/'))  # 按/进行拆分
print(str3.strip())  # 默认去除字符串两边空格或换行符，返回的是字符串
print(type(str3.strip()))

# 原型： re.split(pattern, string, maxsplit=0)   其中还有个flag没列出来，不常用
#
# 通过正则表达式将字符串分离。如果用括号将正则表达式括起来，那么分隔符也会被列入到list中返回。
# maxsplit是分离的次数，maxsplit=1分离一次，默认为0，不限制次数


import re

str4 = 'i _ , /d f'
str5 = 'aaa bbb ccc;ddd  eee,fff'
print(re.split(r'\W+', str4))  # 去除除了是字母或数字或下划线或汉字以外的字符
print(re.split(r'\s+', str5))  # 去除空格
print(re.split(r'[_/]', str4))  # 分隔符为下划线和/
print(re.split(r'([_/])', str4))  # 分隔符为下划线和/，但保留分隔符
