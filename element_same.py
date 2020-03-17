# 统计列表中元素的频率
# Counter函数可以用来判断字符串中包含的元素是否相同，无论字符串中元素顺序如何，只要包含相同的元素和数量，就认为其是相同的


from collections import Counter
str1, str2, str3 = "python", "pyhton", "onpyth"
cnt1, cnt2, cnt3 = Counter(str1), Counter(str2), Counter(str3)
if cnt1 == cnt2 and cnt2 == cnt3:
    print("三个字符串元素相同")
else:
    print("不相同")