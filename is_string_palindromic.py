# 判断字符串是否是回文
# 利用字符串的翻转来判断字符是否是回文字符串
# string_reversal为字符串翻转

import string_reversal as sr

str1 = 'abcba'
str2 = 'andsf'

def fun(str):
    if str == sr.method1(str):
        print(str + "是回文串")
    else:
        print(str + '不是回文串')


fun(str1)
fun(str2)
