# 字符串拆分
# 字符串的拆分可以直接利用split函数，进行实现，返回的是列表
# 而strip函数用于移除字符串头尾指定的字符（默认为空格或换行符）


str1 = 'i love python'
str2 = 'i/love/python'
str3 = '  i love python   ' \
       ''
print(str1.split()) # 默认按空格拆分，返回的是列表
print(str2.split('/')) # 按/进行拆分
print(str3.strip()) # 默认去除字符串两边空格或换行符，返回的是字符串
print(type(str3.strip()))
