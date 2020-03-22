# 检查唯一性
# 通过检查列表长度是否与set后的列表长度一致，来判断列表中的元素是否是独一无二的


def ifUnique(seq):
    if len(seq) == len(set(seq)):
        print("该列表中元素是唯一的")
    else:
        print("该列表中元素是不唯一的")


lst1 = [1, 2, 3, 4, 5]
lst2 = [1, 1, 2, 3, 4]
ifUnique(lst1)
ifUnique(lst2)
